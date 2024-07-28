from stdtest import *
import collections
import contextlib
from concurrent.futures import Future
import aiofiles
import collections.abc
import tempfile
import glob
from stdtest.tasksubmitter import combine


class CcException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__()
        self.msg = msg


@dataclasses.dataclass
class Node:
    io: io.IOBase
    desc: str

    def close(self):
        self.io.close()

    def __hash__(self) -> int:
        return hash(self.io.fileno())

    def __eq__(self, othr: object) -> bool:
        return type(othr) is Node and self.io.fileno() == othr.io.fileno()


lock = threading.Lock()


@dataclasses.dataclass
class Process:
    cmd: str | List[str]
    desc: str
    p: Popen = None

    def __post_init__(self):
        # with lock:  # TODO Make os.pipe thread-safe ???
        self.p = Popen(
            self.cmd,
            stdin=PIPE,
            stdout=PIPE,
            stderr=PIPE,
            shell=type(self.cmd) is str,
        )

    @property
    def stdin(self):
        return Node(self.p.stdin, desc=f"{self.desc}/stdin")

    @property
    def stdout(self):
        return Node(self.p.stdout, desc=f"{self.desc}/stdout")

    @property
    def stderr(self):
        return Node(self.p.stderr, desc=f"{self.desc}/stderr")

    def poll(self):
        return self.p.poll()

    def terminate(self):  # TODO
        self.p.stdin.close()  # Necessary to terminal children processes of docker exec.
        self.p.stdout.close()
        self.p.stderr.close()
        self.p.terminate()
        # self.p.kill()

    @property
    def pid(self):
        return self.p.pid

    @property
    def returncode(self):
        return self.p.returncode


async def flow(
    s: Node,
    ts: List[Node],
    task: Task = None,
):
    t = None
    try:
        async with contextlib.AsyncExitStack() as stack:
            r = await stack.enter_async_context(
                aiofiles.open(s.io.fileno(), "rb", closefd=F, buffering=0)
            )
            ws = [
                (
                    t,
                    await stack.enter_async_context(
                        aiofiles.open(t.io.fileno(), "ab", closefd=F, buffering=0)
                    ),
                )
                for t in ts
            ]
            while T:
                c = await r.read(conf.bytes_per_read)
                if not c:
                    break
                print(c)
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
            logger.error(f"Edge[{s.desc} > {t.desc if t else '*'}] ERROR")
            task.solved = F


async def poll(
    proc: Process,
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


def run_graph(coros: List[collections.abc.Coroutine]):
    async def main(coros: List[collections.abc.Coroutine]):
        await asyncio.gather(*coros)

    asyncio.run(main(coros))


build_debug: bool = None


def build(
    task: Task,
):
    def _compile(file: str):
        prefix, suffix = os.path.splitext(file)
        if conf.languages[suffix].interpreted:
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

    with open(logger_file.path, "w") as log:
        log.seek(0)
        log.truncate(0)
        windows["log"].clear_signal.emit()
        print(f"Validating task [{task.name}]...", file=log, flush=T)

        task.solved = T
        for idx, role in enumerate(["solver", "generator", "comparator", "checker", "manual_input"], 1):
            print(f"{idx}. Checking {role.title()}...", end="", file=log, flush=T)
            if global_stopflag.is_set():
                print(f"terminated", file=log, flush=T)
                continue
            file = getattr(task, role)
            file_mustexists = F
            file_mustexists |= role == "solver"
            file_mustexists |= role == "generator" and task.test_type in (TT.BF, TT.G_C)
            file_mustexists |= role == "comparator" and task.test_type == TT.G_C
            file_mustexists |= role == "checker" and task.test_type == TT.IC
            file_mustexists |= role == "manual_input" and task.test_type == TT.MI
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
                    print(f"Error, no file match wildcard [{task.manual_input}]", file=log, flush=T)
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
                f"Validating OK, task will be testing in {task.test_type.value} mode...",
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


def test(task: Task):
    with (
        open(logger_file.path, "a") as log,
        tempfile.NamedTemporaryFile(mode="w+") as input,
        # open("input.txt", "w+") as input,
        tempfile.NamedTemporaryFile(mode="w+") as answer,
        tempfile.NamedTemporaryFile(mode="w+") as actual,
    ):
        vlog = Node(log, "log")
        vanswer = Node(answer, "answer")
        vactual = Node(actual, "actual")
        vinput = Node(input, "input")

        if task.test_type == TT.MI:
            task.cpu = 0
            task.mem = 0
            task.pipe = 0
            proc = Process(
                conf.execute_cmd(task.solver),
                desc="solver",
            )
            print("Input:", file=log, flush=T)
            file = max(glob.glob(task.manual_input), key=os.path.getmtime)
            input.seek(0)
            for line in open(file):
                print(line, end="", file=log)
                print(line, end="", file=input)
            print(file=log, flush=T)
            print(file=input, flush=T)
            input.seek(0)
            print("Output:", file=log, flush=T)
            run_graph(
                [
                    poll(proc, task=task),
                    flow(vinput, [proc.stdin], task=task),
                    flow(proc.stdout, [vactual, vlog]),
                    flow(proc.stderr, [vlog]),
                ]
            )
            print_verdict(log, task, procs=[proc], answer=None, actual=actual)
            
        elif task.test_type == TT.RI_RA:

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

            passed = T
            totcpu, maxmem = 0, 0
            tid = 1
            for test_input, test_answer in zip(
                blank_lines_seperated(task.test_input),
                blank_lines_seperated(task.test_output),
            ):

                task.cpu = 0
                task.mem = 0
                task.pipe = 0
                for file in [input, answer, actual]:
                    file.seek(0)
                    file.truncate(0)
                print(f"\nTest #{tid}:", file=log, flush=T)
                proc = Process(
                    conf.execute_cmd(task.solver),
                    desc="solver",
                )
                print("Input:", file=log, flush=T)
                print(test_input, file=log, flush=T)
                print(test_input, file=input, flush=T)
                input.seek(0)
                print("Answer:", file=log, flush=T)
                print(test_answer, file=log, flush=T)
                print(test_answer, file=answer, flush=T)
                print("Actual:", file=log, flush=T)
                # vinput = Node(input, "input")
                # vactual = Node(actual, "actual")
                # vlog = Node(log, "log")
                run_graph(
                    [
                        poll(proc, task=task),
                        flow(vinput, [proc.stdin], task=task),
                        flow(proc.stdout, [vactual, vlog]),
                        flow(proc.stderr, [vlog]),
                    ]
                )
                totcpu += task.cpu
                maxmem = max(maxmem, task.mem)
                print_verdict(log, task, procs=[proc], answer=answer, actual=actual)
                passed &= task.solved
                tid += 1
                if global_stopflag.is_set():
                    print("\tterminated", file=log, flush=T)
                    return
            # clear input
            input.seek(0)
            input.truncate(0)
            print_conclusion(log, passed, totcpu, maxmem)
        elif task.test_type in (TT.G_C, TT.BF):
            
            tid = 1
            totcpu, maxmem = 0, 0
            while T:
                # log.seek(0)
                # log.truncate(0)
                # windows["fileViewer"].clear_signal.emit()
                print(f"\nTest #{tid}:", file=log, flush=T)
                # run last failed first (if exists)
                input.seek(0)
                last_fail_input = "lastfail.txt"
                if os.path.exists(last_fail_input) and os.path.getsize(last_fail_input) > 0:
                    print("Input: (Retry last fail)", file=log, flush=T)
                    for line in open(last_fail_input):
                        print(line, end="", file=input)
                        print(line, end="", file=log)
                    print(file=input, flush=T)
                    print(file=log, flush=T)
                    # clear
                    with open(last_fail_input, "w") as w:
                        pass
                else:
                    print("Input: (Generator)", file=log, flush=T)
                    pG = Process(
                        conf.execute_cmd(task.generator),
                        desc="generator",
                    )
                    run_graph(
                        [
                            poll(pG),
                            flow(pG.stdout, [vinput, vlog]),
                            flow(pG.stderr, [vlog]),
                        ]
                    )
                    if pG.returncode:
                        print_verdict(
                            log, task, procs=[pG], answer=answer, actual=actual
                        )
                        break
                if task.test_type == TT.BF:
                    pass
                else:
                    input.seek(0)
                    print("Answer:", file=log, flush=T)
                    answer.seek(0)
                    answer.truncate(0)
                    pC = Process(
                        conf.execute_cmd(task.comparator),
                        desc="comparator",
                    )
                    run_graph(
                        [
                            poll(pC),
                            flow(vinput, [pC.stdin]),
                            flow(pC.stdout, [vanswer, vlog]),
                            flow(pC.stderr, [vlog]),
                        ]
                    )
                    if pC.returncode:
                        print_verdict(
                            log, task, procs=[pC], answer=answer, actual=actual
                        )
                        return
                input.seek(0)
                print("Actual:", file=log, flush=T)
                actual.seek(0)
                actual.truncate(0)
                proc = Process(
                    conf.execute_cmd(task.solver),
                    desc="solver",
                )
                run_graph(
                    [
                        poll(proc, task=task),
                        flow(vinput, [proc.stdin], task=task),
                        flow(proc.stdout, [vactual, vlog]),
                        flow(proc.stderr, [vlog]),
                    ]
                )
                print_verdict(
                    log,
                    task,
                    procs=[proc],
                    answer=(None if task.test_type == TT.BF else answer),
                    actual=actual,
                )
                passed = task.solved
                if not passed:
                    input.seek(0)
                    with open(last_fail_input, "w") as w:
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
                    print_conclusion(log, T, totcpu, maxmem)
                    break

        elif task.test_type == TT.IC:
            tid = 1
            totcpu, maxmem = 0, 0
            while T:
                # log.seek(0)
                # log.truncate(0)
                # windows["fileViewer"].clear_signal.emit()
                print(f"\nTest #{tid}:", file=log, flush=T)
                input.seek(0)
                last_fail_input = "lastfail.txt"
                # run last failed first (if exists)
                if os.path.exists(last_fail_input) and os.path.getsize(last_fail_input) > 0:
                    print("Input: (Retry last fail)", file=log, flush=T)
                    for line in open(last_fail_input):
                        print(line, end="", file=input)
                        print(line, end="", file=log)
                    print(file=input, flush=T)
                    print(file=log, flush=T)
                    # clear
                    with open(last_fail_input, "w") as w:
                        pass
                else:
                    print("Input: (Generator)", file=log, flush=T)
                    pG = Process(
                        conf.execute_cmd(task.generator),
                        desc="generator",
                    )
                    run_graph(
                        [
                            poll(pG),
                            flow(pG.stdout, [vinput, vlog]),
                            flow(pG.stderr, [vlog]),
                        ]
                    )
                    if pG.returncode:
                        print_verdict(
                            log, task, procs=[proc], answer=answer, actual=actual
                        )
                        break
                input.seek(0)
                print("Chat:", file=log, flush=T)
                pSolver = Process(
                    conf.execute_cmd(task.solver),
                    desc="solver",
                )
                pChecker = Process(
                    conf.execute_cmd(task.ichecker),
                    desc="checker",
                )
                run_graph(
                    [
                        poll(pSolver, task=task),
                        poll(pChecker),
                        flow(vinput, [pChecker.stdin]),
                        flow(pChecker.stdout, [pSolver.stdin, vlog]),
                        flow(pSolver.stdout, [pChecker.stdin, vlog]),
                        flow(pChecker.stderr, [vlog]),
                        flow(pSolver.stderr, [vlog]),
                    ]
                )
                print_verdict2(log, task, pSolver, pChecker)
                passed = task.solved
                if not passed:
                    input.seek(0)
                    with open(last_fail_input, "w") as w:
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
                    print_conclusion(log, T, totcpu, maxmem)
                    break


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
    log: io.TextIOBase,
    task: Task,
    procs: List[Process],
    answer: io.TextIOBase,
    actual: io.TextIOBase,
):
    print("Verdict ", end="", file=log)
    if not task.solved:
        print("Node/Edge Error", file=log, flush=T)
        return
    if global_stopflag.is_set():
        print("Terminated", file=log, flush=T)
        return
    for proc in procs:
        if proc.returncode:
            print(
                f"Runtime error(Proc[{proc.desc}] exited with code {proc.returncode})",
                file=log,
                flush=T,
            )
            task.solved = F
            return
    if answer and not compare_tokens(answer, actual):
        task.solved = F
        print("Fails: Wrong Answer", file=log, flush=T)
    elif task.mem > task.mem_limit:
        task.solved = F
        print(f"Fails: Memory limit exceeded ({task.mem} > {task.mem_limit})")
    elif task.cpu > task.cpu_limit:
        task.solved = F
        print(f"Fails: Time limit exceeded ({task.cpu} > {task.cpu_limit})", file=log, flush=T)
    else:
        status = "Answer is unknown" if not answer else "OK"
        print(f"{status} in {task.cpu}s & {task.mem}mB", file=log, flush=T)


def print_conclusion(log: io.TextIOBase, allpassed: bool, totcpu: int, maxmem: int):
    # if global_stopflag.is_set():
    #     return
    # print("Conclusion:", file=log)
    print(
        (f"\nAll tests passed " if allpassed else "Some tests failed "),
        end="",
        file=log,
    )
    print(f"in total {round(totcpu, 3)} seconds & max {maxmem} megabytes.", file=log, flush=T)


def print_verdict2(
    log: io.TextIOBase,
    task: Task,
    psolver: Process,
    pjurger: Process,
):
    print("Verdict ", end="", file=log)
    if not task.solved:
        print("Fails: Node/Edge Error", file=log, flush=T)
        return
    if global_stopflag.is_set():
        print("Terminated", file=log, flush=T)
        return
    rsolver = psolver.returncode
    rjurger = pjurger.returncode
    if rsolver:
        print(
            "Fails: "
            "A solution finishing with exit code other than 0 (without exceeding time \n"
            "or memory limits) would be interpreted as a Runtime Error in the system.",
            file=log,
            flush=T,
        )
        task.solved = F
    elif rjurger:
        print(
            "Fails: "
            "A solution finishing with exit code 0 (without exceeding time \n"
            "or memory limits) and a judge finishing with exit code other \n"
            "than 0 would be interpreted as a Wrong Answer (or query limit exceeded) \n"
            "in the system.\n",
            file=log,
            flush=T,
        )
        task.solved = F
    elif task.mem > task.mem_limit:
        print(f"Fails: Memory limit exceeded ({task.mem} > {task.mem_limit})")
        task.solved = F
    elif task.cpu > task.cpu_limit:
        print(f"Fails: Time limit exceeded ({task.cpu} > {task.cpu_limit})", file=log, flush=T)
        task.solved = F
    else:
        print(f"OK in {task.cpu}s & {task.mem}mB", file=log, flush=T)

