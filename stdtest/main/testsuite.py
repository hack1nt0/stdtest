from PySide6.QtGui import QCloseEvent
from stdtest import *
from stdtest.taskfinder import TaskFinderD
from stdtest.tasksubmitter import CodeSubmitter
from .statemachines import *
from PySide6.QtSvgWidgets import QSvgWidget
from stdtest.taskeditor import TaskEditor
from .inputbox import InputBox
from stdtest.taskeditor import RunConfirmD
from stdtest.listener import TaskCreatorD
from .testsuite_ui import Ui_TestSuite


class TestSuite(QWidget, Ui_TestSuite):
    run_task_signal: Signal = Signal(dict)

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        self.tasks = []
        self.tasksbox.currentIndexChanged.connect(self.change_task)
        self.taskfinderd = TaskFinderD(self)
        self.taskfinderd.found_tasks_signal.connect(self.set_tasks)
        self.taskfinderd.hide()
        self.findButton.clicked.connect(self.taskfinderd.show)
        self.findButton.setShortcut("Ctrl+F")
        self.findButton.setIcon(QIcon(paths.img("search.png")))
        self.refreshButton.setIcon(QIcon(paths.img("sync.png")))
        self.refreshButton.clicked.connect(self.taskfinderd.refresh)
        self.rootButton.setIcon(QIcon(paths.img("folder.png")))
        self.rootButton.clicked.connect(self.pick_tasksdir)
        self.newButton.setIcon(QIcon(paths.img("add.png")))
        self.newButton.clicked.connect(self.new_task)


        # self.stk_shortcut = QShortcut("Alt+O", self)
        # def switch_stk():
        #     cur = self.stackedWidget.currentIndex()
        #     nxt = (cur + 1) % 2
        #     self.stackedWidget.setCurrentIndex(nxt)
        # self.stk_shortcut.activated.connect(switch_stk)
        self.tab_shortcut = QShortcut("Alt+Tab", self)
        def switch_tab():
            cur = self.tabWidget.currentIndex()
            nxt = (cur + 1) % self.tabWidget.count()
            self.tabWidget.setCurrentIndex(nxt)
        self.tab_shortcut.activated.connect(switch_tab)

        ### TEST
        self.testButton.setToolTip("Test (Ctrl+R)")
        self.testButton.setIcon(QIcon(paths.img("play-button.png")))
        self.testButton.clicked.connect(self.test_task)
        self.testButton.setShortcut("Ctrl+R")
        conf.build_debug = T
        self.terminateButton.clicked.connect(self.terminate_task)
        self.terminateButton.setIcon(QIcon(paths.img("stop-button.png")))
        self.terminateButton.setVisible(F)

        ### SUBMIT
        self.copyButton.setShortcut("F7")
        self.copyButton.setToolTip("Submit/Copy (F7)")
        self.copyButton.setIcon(QIcon(paths.img("send.png")))
        self.copyButton.clicked.connect(self.copy_task)

        self.tabWidget.setEnabled(F)
        if not conf.tasks_dir:
            self.findButton.setEnabled(F)
            self.refreshButton.setEnabled(F)
            self.newButton.setEnabled(F)
        self.log.init()
    
    def pick_tasksdir(self):
        d = QFileDialog(self)
        d.setWindowModality(Qt.WindowModality.WindowModal)
        d.setFileMode(QFileDialog.FileMode.Directory)
        d.setDirectory(conf.tasks_dir)
        d.setWindowTitle("Tasks Subdirectory")
        if d.exec():
            tasksdir = d.selectedFiles()[0]
            conf.tasks_dir = tasksdir

    @property
    def task(self) -> Task | None:
        # return self.editor.task
        return self.tasks[self.tasksbox.currentIndex()] if self.tasks else None
    
    def set_tasks(self, tasks: List[Task]):
        self.tasks = tasks
        self.tasksbox.blockSignals(T)
        self.tasksbox.clear()
        self.tasksbox.addItems(list(map(lambda task: task.name, self.tasks)))
        self.tasksbox.blockSignals(F)
        self.change_task(self.tasksbox.currentIndex())

    def new_task(self, jsondict: dict=None):
        d = TaskCreatorD(self)
        if jsondict:
            d.set_json(jsondict)
        else:
            d.setWindowTitle("New Task")
        d.exec()
        
    def change_task(self, idx: int):
        if idx >= 0:
            self.editor.set_task(self.task)
            self.doceditor.set_task(self.task)
            self.tabWidget.setEnabled(T)
            os.chdir(self.task.path)
        else:
            self.tabWidget.setEnabled(F)

    @property
    def all_btns(self):
        return (
            self.rootButton,
            self.findButton,
            self.refreshButton,
            self.newButton,
            self.testButton,
            self.terminateButton,
            self.copyButton,
        )

    def pre_task(self):
        for w in self.all_btns:
            w.setEnabled(F)
        self.testButton.setVisible(F)
        self.testButton.setEnabled(F)
        self.terminateButton.setVisible(T)
        self.terminateButton.setEnabled(T)
        self.log.init()

    def test_task(self):
        d = RunConfirmD(self)
        d.set_task(self.task)
        if d.exec():
            self.pre_task()
            self.machine = statemachine_of_test(self.task, [])
            # self.machine.started.connect(self.pre_task)
            self.machine.finished.connect(self.post_task)
            self.machine.start()

    def post_task(self):
        for w in self.all_btns:
            w.setEnabled(T)
        self.testButton.setVisible(T)
        self.testButton.setEnabled(T)
        self.terminateButton.setVisible(F)
        self.terminateButton.setEnabled(F)

    def terminate_task(self):
        global_stopflag.set()

    def copy_task(self):
        from stdtest.tasksubmitter import combine
        logger.info("Combining source...")
        src = combine(self.task.solver)
        QGuiApplication.clipboard().setText(src)
        prefix, suffix = os.path.splitext(self.task.solver)
        main = f"Main{suffix}"
        with open(main, "w") as w:
            w.write(src)
        logger.info(src)
        logger.info(f"Combination done: copied to clipboard, and saved as {main}.")
    


