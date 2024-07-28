from stdtest import *
import collections
import contextlib
from concurrent.futures import Future
import aiofiles
import collections.abc
import tempfile
import glob
from stdtest.tasksubmitter import combine


lock = threading.Lock()


def make_process(cmd: str | List[str], desc: str = ""):
    p = Popen(
        cmd,
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,
        shell=type(cmd) is str,
    )
    p.desc = desc
    return p


async def flow(
    s: io.IOBase,
    ts: List[io.IOBase],
    task: Task = None,
):
    t = None
    try:
        async with contextlib.AsyncExitStack() as stack:
            r = await stack.enter_async_context(
                aiofiles.open(s.fileno(), "rb", closefd=F, buffering=0)
            )
            ws = [
                (
                    t,
                    await stack.enter_async_context(
                        aiofiles.open(t.fileno(), "ab", closefd=F, buffering=0)
                    ),
                )
                for t in ts
            ]
            while T:
                c = await r.read(conf.bytes_per_read)
                if not c:
                    break
                # print(c)
                for t, w in ws:
                    await w.write(c)
                if task:
                    task.pipe += len(c)
        # # deal with less input
        # if s.desc == "input":
        #     for t in ts:
        #         t.close()
    except BaseException as e:
        if global_stopflag.is_set():
            print("Terminated", flush=T)
        else:
            global_stopflag.set()
            logger.exception(e)
            # logger.error(f"Edge[{s.desc} > {t.desc if t else '*'}] ERROR")
            task.solved = F


async def poll(
    proc: Popen,
    task: Task = None,
):
    need_metric: bool = proc.desc in ("solver", "compile")
    tic = time.perf_counter()
    pp: psutil.Process = None
    try:
        while T:
            if global_stopflag.is_set():
                proc.terminate()
                return
            if task:
                task.cpu = round((time.perf_counter() - tic), 3)
                try:
                    if pp is None:
                        pp = psutil.Process(proc.pid)
                    task.mem = round(pp.memory_info().rss / 1024 / 1024)
                except:
                    pass
            ret = proc.poll()
            if ret is not None:
                return
            await asyncio.sleep(0)
    except BaseException as e:
        global_stopflag.set()
        logger.error(f"Process[{proc.desc}] ERROR")
        logger.exception(e)
        task.solved = F


def run_graph(*coros: collections.abc.Coroutine):
    async def main(*coros: collections.abc.Coroutine):
        await asyncio.gather(*coros)

    asyncio.run(main(*coros))


build_debug: bool = None


def build(
    task: Task,
):
    def _compile(file: str):
        if conf.language(file).interpreted:
            return 0, ""
        cmd = conf.compile_cmd(file)
        if cmd is None:
            return 1, "No compiler found"
        file_content = combine(file)
        global build_debug
        if (
            file_content == task._combined_files.get(file, None)
            and build_debug == conf.build_debug
        ):
            return 0, "source unchanged"
        try:
            proc = subprocess.run(
                cmd,
                capture_output=T,
                text=T,
            )
            if not proc.returncode:
                task._combined_files[file] = file_content
                build_debug = conf.build_debug
                return 0, ""
            else:
                return proc.returncode, proc.stderr
        except BaseException as e:
            return 1, "".join(traceback.format_exception())

    print(f"Validating task [{task.name}]...", file=log, flush=T)

    task.solved = T
    for idx, role in enumerate(["solver", "generator", "comparator", "ichecker"], 1):
        print(f"{idx}. Checking {role.title()}...", end="", file=log, flush=T)
        if global_stopflag.is_set():
            print(f"terminated", file=log, flush=T)
            continue
        file = getattr(task, role)
        file_mustexists = F
        file_mustexists |= role == "solver"
        file_mustexists |= role == "generator" and task.test_input_type == TT.GENERATOR
        file_mustexists |= (
            role == "comparator" and task.test_answer_type == TT.COMPARATOR
        )
        file_mustexists |= role == "ichecker" and task.test_answer_type == TT.ICHECKER
        if not file_mustexists:
            print(f"OK, unneeded", file=log, flush=T)
        elif not file:
            print(f"Error, not exists", file=log, flush=T)
            task.solved = F
        elif role == "manual_input":
            try:
                file = max(glob.glob(task.manual_input), key=os.path.getmtime)
            except:
                file = None
                pass
            if file:
                print(f"OK, found {file}", file=log, flush=T)
            else:
                print(
                    f"Error, no file match wildcard [{task.manual_input}]",
                    file=log,
                    flush=T,
                )
                task.solved = F
        else:
            returncode, msg = _compile(file)
            if returncode:
                print("compilation error:", file=log)
                print(msg, file=log, flush=T)
                task.solved = F
            elif msg:
                print(f"OK: {msg}", flush=T, file=log)
            else:
                print("OK", file=log, flush=T)
    if global_stopflag.is_set():
        print(f"Validating terminated", file=log, flush=T)
    elif task.solved:
        print(
            f"Validating OK, task will be testing in ({task.test_input_type.value},{task.test_answer_type.value}) mode...",
            file=log,
            flush=T,
        )
    else:
        print(f"Validating error!", file=log, flush=T)


def test_wrapper(task: Task):
    try:
        test(task)
    except Exception as e:
        logger.exception(e)
        global_stopflag.set()


def blank_lines_seperated(string: str):
    r = io.StringIO(string)
    cached = []
    for line in r:
        if not line.strip():
            if cached:
                yield "".join(cached)
                cached.clear()
        cached.append(line)
    if cached:
        yield "".join(cached)
        cached.clear()


def input_iter(task: Task):
    with (tempfile.NamedTemporaryFile(mode="w+") as input,):
        if task.test_input_type == TT.MANUAL:
            for block in blank_lines_seperated(task.test_input):
                input.seek(0)
                input.truncate(0)
                logger.info("Input: (Manual)")
                logger.info(block)
                input.write(block)
                input.seek(0)
                yield input
        elif task.test_input_type == TT.GENERATOR:
            # run last failed first (if exists)
            if os.path.exists(LAST_FAIL_INPUT) and os.path.getsize(LAST_FAIL_INPUT) > 0:
                logger.info("Input: (Last fail input)")
                with open(LAST_FAIL_INPUT) as input:
                    for line in input:
                        logger.info(line[-1])  # TODO
                    input.seek(0)
                    yield input
                    input.seek(0)
                    input.truncate(0)
            while T:
                input.seek(0)
                input.truncate(0)
                logger.info("Input: (Generator)")
                pG = make_process(
                    conf.execute_cmd(task.generator),
                    desc="generator",
                )
                run_graph(
                    poll(pG),
                    flow(pG.stdout, [input, log]),
                    flow(pG.stderr, [log]),
                )
                if pG.returncode:
                    logger.error(f"Generator exit with code {pG.returncode}")
                    return
                input.seek(0)
                yield input
        else:
            yield input


def answer_iter(task: Task):
    with (tempfile.NamedTemporaryFile(mode="w+") as blockio,):
        if task.test_answer_type == TT.MANUAL:
            for block in blank_lines_seperated(task.test_output):
                blockio.seek(0)
                blockio.truncate(0)
                logger.info("Answer: (Manual)")
                logger.info(block)
                blockio.write(block)
                blockio.seek(0)
                yield blockio


def testX0(task: Task):
    passed = T
    totcpu, maxmem = 0, 0
    tid = 1
    with (tempfile.NamedTemporaryFile(mode="w+") as actual,):
        for input, answer in zip(
            input_iter(task),
            answer_iter(task),
        ):
            task.cpu = 0
            task.mem = 0
            task.pipe = 0
            proc = make_process(
                conf.execute_cmd(task.solver),
                desc="solver",
            )
            logger.info("Actual:")
            input.seek(0)
            run_graph(
                poll(proc, task=task),
                flow(input, [proc.stdin], task=task),
                flow(proc.stdout, [actual, log]),
                flow(proc.stderr, [log]),
            )
            totcpu += task.cpu
            maxmem = max(maxmem, task.mem)
            answer.seek(0)
            actual.seek(0)
            print_verdict(tid, task, procs=[proc], answer=answer, actual=actual)
            passed &= task.solved
            tid += 1
            if global_stopflag.is_set():
                logger.info("terminated")
                return
            logger.info("")
    print_conclusion(passed, totcpu, maxmem)


LAST_FAIL_INPUT = "input.txt"


def testX3(task: Task):
    tid = 1
    totcpu, maxmem = 0, 0
    for input in input_iter(task):
        logger.info("Chat:")
        pSolver = make_process(
            conf.execute_cmd(task.solver),
            desc="solver",
        )
        pChecker = make_process(
            conf.execute_cmd(task.ichecker),
            desc="checker",
        )
        run_graph(
            poll(pSolver, task=task),
            poll(pChecker),
            flow(input, [pChecker.stdin]),
            flow(pChecker.stdout, [pSolver.stdin, log]),
            flow(pSolver.stdout, [pChecker.stdin, log]),
            flow(pChecker.stderr, [log]),
            flow(pSolver.stderr, [log]),
        )
        print_verdict2(tid, task, pSolver, pChecker)
        passed = task.solved
        if not passed:
            input.seek(0)
            with open(LAST_FAIL_INPUT, "w") as w:
                for line in input:
                    w.write(line)
            break
        # clear input
        input.seek(0)
        input.truncate(0)
        tid += 1
        totcpu += task.cpu
        maxmem = max(maxmem, task.mem)
        if global_stopflag.is_set():
            print_conclusion(T, totcpu, maxmem)
            with open(LAST_FAIL_INPUT, "w") as w:
                pass  # clear
            break
        logger.info("")


def testX2(task: Task):
    tid = 1
    totcpu, maxmem = 0, 0
    with (
        tempfile.NamedTemporaryFile(mode="w+") as actual,
        tempfile.NamedTemporaryFile(mode="w+") as answer,
    ):
        for input in input_iter(task):
            logger.info("Answer:")
            answer.seek(0)
            answer.truncate(0)
            pComp = make_process(
                conf.execute_cmd(task.comparator),
                desc="comparator",
            )
            run_graph(
                poll(pComp),
                flow(input, [pComp.stdin]),
                flow(pComp.stdout, [answer, log]),
                flow(pComp.stderr, [log]),
            )
            if pComp.returncode:
                print_verdict(log, task, procs=[pComp], answer=answer, actual=actual)
                return
            input.seek(0)
            logger.info("Actual:")
            actual.seek(0)
            actual.truncate(0)
            pSolver = make_process(
                conf.execute_cmd(task.solver),
                desc="solver",
            )
            run_graph(
                poll(pSolver, task=task),
                flow(input, [pSolver.stdin], task=task),
                flow(pSolver.stdout, [actual, log]),
                flow(pSolver.stderr, [log]),
            )
            actual.seek(0)
            answer.seek(0)
            print_verdict(
                tid,
                task,
                procs=[pSolver],
                answer=answer,
                actual=actual,
            )
            passed = task.solved
            if not passed:
                input.seek(0)
                with open(LAST_FAIL_INPUT, "w") as w:
                    for line in input:
                        w.write(line)
                break
            # clear input
            input.seek(0)
            input.truncate(0)
            tid += 1
            totcpu += task.cpu
            maxmem = max(maxmem, task.mem)
            if global_stopflag.is_set():
                print_conclusion(T, totcpu, maxmem)
                with open(LAST_FAIL_INPUT, "w") as w:
                    pass
                break
            logger.info("")


def testX4(task: Task):
    passed = T
    totcpu, maxmem = 0, 0
    tid = 1
    with (tempfile.NamedTemporaryFile(mode="w+") as actual,):
        for input in input_iter(task):
            task.cpu = 0
            task.mem = 0
            task.pipe = 0
            proc = make_process(
                conf.execute_cmd(task.solver),
                desc="solver",
            )
            logger.info("Actual:")
            input.seek(0)
            run_graph(
                poll(proc, task=task),
                flow(input, [proc.stdin], task=task),
                flow(proc.stdout, [actual, log]),
                flow(proc.stderr, [log]),
            )
            totcpu += task.cpu
            maxmem = max(maxmem, task.mem)
            actual.seek(0)
            print_verdict(tid, task, procs=[proc], answer=None, actual=actual)
            passed &= task.solved
            tid += 1
            if global_stopflag.is_set():
                logger.info("terminated")
                return
            logger.info("")
    print_conclusion(passed, totcpu, maxmem)
    pass


def test(task: Task):
    match task.test_answer_type:
        case TT.MANUAL:
            testX0(task)
        case TT.ICHECKER:
            testX3(task)
        case TT.COMPARATOR:
            testX2(task)
        case TT.UNKNOWN:
            testX4(task)


def compare_tokens(answer: io.TextIOBase, actual: io.TextIOBase) -> bool:
    def tokens(stream):
        for line in stream:
            for tk in line.split():
                yield tk

    answer.seek(0)
    actual.seek(0)
    import itertools

    for atoken, btoken in itertools.zip_longest(tokens(answer), tokens(actual)):
        ret = F
        if atoken and btoken:
            try:
                ret = abs(float(atoken) - float(btoken)) < 1e-6
            except ValueError:
                ret = atoken == btoken
        if not ret:
            return F
    return T


def print_verdict(
    tid: int,
    task: Task,
    procs: List[Popen],
    answer: io.TextIOBase,
    actual: io.TextIOBase,
):
    logger.info(f"Test #{tid} verdict:")
    if not task.solved:
        logger.info("Node/Edge Error")
        return
    if global_stopflag.is_set():
        logger.info("Terminated")
        return
    for proc in procs:
        if proc.returncode:
            logger.info(
                f"Runtime error(Proc[{proc.desc}] exited with code {proc.returncode})",
            )
            task.solved = F
            return
    if answer and not compare_tokens(answer, actual):
        task.solved = F
        logger.info("Fails: Wrong Answer")
    elif task.mem > task.mem_limit:
        task.solved = F
        logger.info(f"Fails: Memory limit exceeded ({task.mem} > {task.mem_limit})")
    elif task.cpu > task.cpu_limit:
        task.solved = F
        logger.info(f"Fails: Time limit exceeded ({task.cpu} > {task.cpu_limit})")
    else:
        status = "Answer is unknown" if not answer else "OK"
        logger.info(f"{status} in {task.cpu}s & {task.mem}mB")


def print_conclusion(allpassed: bool, totcpu: int, maxmem: int):
    # if global_stopflag.is_set():
    #     return
    # print("Conclusion:", file=log)
    logger.info(
        (f"\nAll tests passed " if allpassed else "Some tests failed "),
    )
    logger.info(f"in total {round(totcpu, 3)} seconds & max {maxmem} megabytes.")


def print_verdict2(
    tid: int,
    task: Task,
    psolver: Popen,
    pjurger: Popen,
):
    logger.info(f"Test #{tid} verdict:")
    if not task.solved:
        logger.info("Fails: Node/Edge Error")
        return
    if global_stopflag.is_set():
        logger.info("Terminated")
        return
    rsolver = psolver.returncode
    rjurger = pjurger.returncode
    if rsolver:
        logger.info(
            "Fails: "
            "A solution finishing with exit code other than 0 (without exceeding time \n"
            "or memory limits) would be interpreted as a Runtime Error in the system.",
        )
        task.solved = F
    elif rjurger:
        logger.info(
            "Fails: "
            "A solution finishing with exit code 0 (without exceeding time \n"
            "or memory limits) and a judge finishing with exit code other \n"
            "than 0 would be interpreted as a Wrong Answer (or query limit exceeded) \n"
            "in the system.\n",
        )
        task.solved = F
    elif task.mem > task.mem_limit:
        logger.info(f"Fails: Memory limit exceeded ({task.mem} > {task.mem_limit})")
        task.solved = F
    elif task.cpu > task.cpu_limit:
        logger.info(
            f"Fails: Time limit exceeded ({task.cpu} > {task.cpu_limit})",
        )
        task.solved = F
    else:
        logger.info(f"OK in {task.cpu}s & {task.mem}mB")
