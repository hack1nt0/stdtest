from PySide6.QtGui import QCloseEvent
from stdtest import *
from stdtest.taskfinder import TaskFinderD
from stdtest.taskbrowser import TaskListBrowserD
from stdtest.tasksubmitter import CodeSubmitter
from .statemachines import *
from PySide6.QtSvgWidgets import QSvgWidget
from stdtest.taskeditor import TaskEditor
from .inputbox import InputBox
from stdtest.taskeditor import RunConfirmD
from .testsuite_ui import Ui_TestSuite


class TestSuite(QWidget, Ui_TestSuite):
    run_task_signal: Signal = Signal(dict)

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        # for btn in self.all_btns:
        #     # btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon if btn.text() else Qt.ToolButtonStyle.ToolButtonIconOnly)
        #     btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        # self.pickButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        ### HELP
        self.helpButton.setToolTip("Help (F1)")
        self.helpButton.setShortcut("F1")
        self.helpButton.setIcon(QIcon(paths.img("question.png")))
        self.helpButton.clicked.connect(
            lambda: QDesktopServices.openUrl(
                # "https://time-oviraptor-66c.notion.site/cchelper-a8b256d6d2534c609f04d15a7f8e95f0"
                "https://github.com/hack1nt0/cchelper"
            )
        )

        # self.taskFinder = TaskFinderD(self)
        # self.taskBrowser = TaskListBrowserD(self)
        # self.taskFinder.find_task_signal.connect(self.taskBrowser.find_task)
        # self.taskBrowser.pick_task_signal.connect(self.set_task)
        # self.taskFinder.hide()
        # self.taskBrowser.hide()
        # self.syncButton.setIcon(QIcon(paths.img("sync.png")))
        # self.syncButton.clicked.connect(self.cloud_sync)
        self.findButton.clicked.connect(self.find_task)
        self.findButton.setShortcut("Ctrl+F")
        self.findButton.setIcon(QIcon(paths.img("search.png")))
        self.pickButton.clicked.connect(self.pick_task)
        self.pickButton.setIcon(QIcon(paths.img("folder.png")))

        self.stk_shortcut = QShortcut("Alt+O", self)
        def switch_stk():
            cur = self.stackedWidget.currentIndex()
            nxt = (cur + 1) % 2
            self.stackedWidget.setCurrentIndex(nxt)
        self.stk_shortcut.activated.connect(switch_stk)

        ### TEST
        self.testButton.setShortcut("F5")
        self.testButton.setToolTip("Test (F5)")
        self.testButton.setIcon(QIcon(paths.img("play-button.png")))
        self.testButton.clicked.connect(self.test_task)
        conf.build_debug = T
        self.terminateButton.clicked.connect(self.terminate_task)
        self.terminateButton.setIcon(QIcon(paths.img("stop-button.png")))
        self.terminateButton.setVisible(F)

        ### SUBMIT
        self.copyButton.setShortcut("F7")
        self.copyButton.setToolTip("Submit/Copy (F7)")
        self.copyButton.setIcon(QIcon(paths.img("send.png")))
        self.copyButton.clicked.connect(self.copy_task)

        ### VERDICT
        # self.chartButton.setIcon(QIcon(paths.img("pie-chart.png")))
        # self.addButton.setIcon(QIcon(paths.img("add.png")))

        # windows["log"] = self.log

        # def open_link(url: str):
        #     if url.startswith("http"):
        #         QDesktopServices.openUrl(url)
        #     else:
        #         self.pick_task()
        # self.label.linkActivated.connect(open_link)

        self.tabWidget.setTabsClosable(T)
        def close_tab(idx: int):
            tab = self.tabWidget.widget(idx)
            tab.close()
            self.tabWidget.removeTab(idx)
        self.tabWidget.tabCloseRequested.connect(close_tab)
        self.tab_shortcut = QShortcut("Alt+Tab", self)
        def switch_tab():
            cur = self.tabWidget.currentIndex()
            nxt = (cur + 1) % self.tabWidget.count()
            self.tabWidget.setCurrentIndex(nxt)
        self.tab_shortcut.activated.connect(switch_tab)
        def change_task(idx: int):
            os.chdir(self.task.path)
            logger.info(f"PWD change to {self.task.path}")
        self.tabWidget.currentChanged.connect(change_task)

        self.log.init()

        os.chdir(os.path.expanduser("~"))

        self.add_task(load_task_from_json("/Users/dy/gits/cc/D.Cat,FoxandMaximumArraySplit2"))
    
    def add_task(self, task: Task):
        for idx in range(self.tabWidget.count()):
            editor = self.tabWidget.widget(idx)
            if editor.task.name == task.name:
                self.tabWidget.setCurrentIndex(idx)
                return
        editor = TaskEditor(self)
        editor.set_task(task)
        self.tabWidget.addTab(editor, task.name)
        self.tabWidget.setCurrentWidget(editor)
    
    @property
    def editor(self) -> TaskEditor | None:
        return self.tabWidget.currentWidget() if self.tabWidget.count() else None

    @property
    def task(self) -> Task | None:
        # return self.editor.task
        return self.tasks[self.tasksbox.currentIndex]
    
    def set_tasks(self, tasks: List[Task]):
        self.tasks = tasks
        self.tasksbox.blockSignals(T)
        self.tasksbox.clear()
        self.tasksbox.addItems(list(map(lambda task: task.name, self.tasks)))
        self.tasksbox.blockSignals(F)
        if self.tasks:
            self.editor.setEnabled(T)
            self.change_task(0)
        else:
            self.editor.setEnabled(F)
        
    def change_task(self, idx: int):
        self.editor.set_task(self.task)
        os.chdir(self.task.path)

    def pick_task(self):
        d = QFileDialog(self)
        d.setWindowModality(Qt.WindowModality.WindowModal)
        # d.setDirectory(os.getcwd())
        d.setFileMode(QFileDialog.FileMode.Directory)
        d.setWindowTitle("Pick a task")
        if d.exec():
            path = d.selectedFiles()[0]
            self.add_task(load_task_from_json(path))

    @property
    def all_btns(self):
        return (
            self.helpButton,
            self.findButton,
            self.pickButton,
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
        self.editor.save_task()
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
    
    def find_task(self):
        log.seek(0)
        log.truncate(0)
        d = TaskFinderD(self)
        if d.exec():
            self.tasks = d.founds

    def arxiv_task(self):
        pass

    def cloud_sync(self):
        pass


