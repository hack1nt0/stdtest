from stdtest import *
import stdtest.main.testsync as TestService

__all__ = [
    "statemachine_of_build",
    "statemachine_of_test",
]

class ThreadedState(QState):
    ok_signal: Signal = Signal()

    def __init__(self, fn, *args, parent: QState = None) -> None:
        super().__init__(parent)
        self.fn = fn
        self.args = args
        self.entered.connect(self.start)
        self.futures: List[Future] = []

    def start(self):
        global_stopflag.clear()
        self.timer = QTimer(self)
        self.timer.setInterval(1000 // conf.refresh_rate)
        self.timer.timeout.connect(self.refresh)
        self.threadpool = ThreadPoolExecutor(max_workers=1)
        task = self.threadpool.submit(
            self.fn,
            *self.args,
        )
        self.futures.append(task)
        self.timer.start()

    def refresh(self):
        # self.timer.stop()  # TODO
        if all(future.done() for future in self.futures):
            self.stop()
            self.ok_signal.emit()
            return
        # self.timer.start()

    def stop(self):
        self.timer.stop()
        self.futures.clear()
        self.threadpool.shutdown(wait=T, cancel_futures=T)

class BuildState(QState):
    ok_signal: Signal = Signal()
    nk_signal: Signal = Signal()
    skip_signal: Signal = Signal()

    def __init__(self, task: Task, views: List[QWidget], parent: QState = None) -> None:
        super().__init__(parent)
        self.task = task
        self.views = views
        self.entered.connect(self.start)
        self.futures: List[Future] = []

    def start(self):
        global_stopflag.clear()
        for view in self.views:
            view.start("Build")
        self.timer = QTimer(self)
        self.timer.setInterval(1000 // conf.refresh_rate)
        self.timer.timeout.connect(self.refresh)
        self.threadpool = ThreadPoolExecutor(max_workers=conf.parallel)
        task = self.threadpool.submit(
            TestService.build,
            self.task,
        )
        self.futures.append(task)
        self.timer.start()

    def refresh(self):
        self.timer.stop()  # TODO
        if all(future.done() for future in self.futures):
            if self.task.solved:
                self.stop()
                self.ok_signal.emit()
            else:
                self.stop()
                self.nk_signal.emit()
            return
        self.timer.start()

    def stop(self):
        self.timer.stop()
        self.futures.clear()
        self.threadpool.shutdown(wait=T, cancel_futures=T)


class DumpState(QState):
    ok_signal: Signal = Signal()

    def __init__(self, task: Task, views: List[QWidget], parent: QState = None) -> None:
        super().__init__(parent)
        self.task = task
        self.views = views
        self.entered.connect(self.start)
        self.timer = QTimer(self)
        self.timer.setInterval(1000 // conf.refresh_rate)
        self.timer.timeout.connect(self.refresh)
        self.timer2 = QTimer(self)
        self.timer2.setInterval(conf.exe_dump_delay * 1000)
        self.timer2.timeout.connect(self.stop)

    def start(self):
        if global_stopflag.is_set():
            logger.info("Dump Skipped")
            return
        logger.info(f"Dump for {conf.exe_dump_delay}s")
        for view in self.views:
            view.start("Dump")
        self.timer.start()
        self.timer2.start()

    def refresh(self):
        for view in self.views:
            view.refresh()

    def stop(self):
        self.timer.stop()
        self.timer2.stop()
        for view in self.views:
            view.refresh()
            view.stop()
        self.ok_signal.emit()


class WarmState(QState):
    ok_signal: Signal = Signal()

    def __init__(self, task: Task, views: List[QWidget], parent: QState = None) -> None:
        super().__init__(parent)
        self.task = task
        self.views = views
        self.entered.connect(self.start)
        self.timer = QTimer(self)
        self.timer.setInterval(1000 // conf.refresh_rate)
        self.timer.timeout.connect(self.refresh)
        self.timer2 = QTimer(self)
        self.timer2.setInterval(conf.exe_warm_delay * 1000)
        self.timer2.timeout.connect(self.stop)

    def start(self):
        for view in self.views:
            view.start("Warm up")
        self.proc = TestService.Process(self.task.solver.execute_cmd, "warmup")
        self.timer.start()
        self.timer2.start()

    def refresh(self):
        for view in self.views:
            view.refresh()

    def stop(self):
        self.timer.stop()
        self.timer2.stop()
        self.proc.terminate()
        for view in self.views:
            view.refresh()
            view.stop()
        self.ok_signal.emit()


class TestState(QState):
    ok_signal: Signal = Signal()

    def __init__(self, task: Task, views: List[QWidget], parent: QState = None) -> None:
        super().__init__(parent)
        self.task = task
        self.views = views
        self.entered.connect(self.start)
        self.futures: List[Future] = []

    def start(self):
        for view in self.views:
            view.start("Run")
        self.timer = QTimer(self)
        self.timer.setInterval(1000 // conf.refresh_rate)
        self.timer.timeout.connect(self.refresh)
        self.threadpool = ThreadPoolExecutor(max_workers=conf.parallel)

        task = self.threadpool.submit(
            TestService.test_wrapper,
            self.task,
        )
        self.futures.append(task)
        for view in self.views:
            view.set_task(self.task)
        self.timer.start()

    def refresh(self):
        self.timer.stop()
        if all(future.done() for future in self.futures):
            self.stop()
            self.ok_signal.emit()
            return
        for view in self.views:
            view.refresh()
        self.timer.start()

    def stop(self):
        self.timer.stop()
        self.futures.clear()
        self.threadpool.shutdown(wait=T, cancel_futures=T)
        for view in self.views:
            view.refresh()
            view.stop()


def statemachine_of_build(task: Task, views: List[QWidget]) -> QStateMachine:
    machine = QStateMachine()
    B = BuildState(task, views)
    T = QFinalState()
    B.addTransition(B, SIGNAL("nk_signal()"), T)
    B.addTransition(B, SIGNAL("ok_signal()"), T)
    B.addTransition(B, SIGNAL("skip_signal()"), T)
    machine.addState(B)
    machine.addState(T)
    machine.setInitialState(B)
    return machine


def statemachine_of_test(task: Task, views: List[QWidget]) -> QStateMachine:
    machine = QStateMachine()
    B = BuildState(task, views)
    # D = DumpState(task, views)
    # W = WarmState(task, views)
    R = ThreadedState(TestService.test_wrapper, task)
    T = QFinalState()
    B.addTransition(B, SIGNAL("nk_signal()"), T)
    # B.addTransition(B, SIGNAL("skip_signal()"), R)
    B.addTransition(B, SIGNAL("ok_signal()"), R)
    # D.addTransition(D, SIGNAL("ok_signal()"), R)
    # W.addTransition(W, SIGNAL("ok_signal()"), R)
    R.addTransition(R, SIGNAL("ok_signal()"), T)
    # B.addTransition(B, SIGNAL("ok_signal()"), R)
    # R.addTransition(R, SIGNAL("ok_signal()"), T)
    for state in [B, R, T]:
        machine.addState(state)
    machine.setInitialState(B)
    return machine
