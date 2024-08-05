from stdtest import *
import glob
from .taskfinder_ui import Ui_TaskFinder


class TaskFinderD(QDialog, Ui_TaskFinder):
    found_tasks_signal: Signal = Signal(list)

    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setModal(T)
        # self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        self.label.setStyleSheet("color: blue")

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
        self.buttonBox.button(QDialogButtonBox.StandardButton.Ok).clicked.connect(
            lambda: self.done(1)
        )
        # self.label.setStyleSheet("background-color : blue; color : white;")

        self.tagsComboBox.addItems(conf.tags)


    def show(self) -> None:
        self.grouplineEdit.setText(conf.find_group)
        self.urlLineEdit.setText(conf.find_url)
        self.nameLineEdit.setText(conf.find_name)

        self.tagsComboBox.setCurrentIndex(conf.find_tags)
        self.cTimeLEdit.setDate(QDateTime.fromSecsSinceEpoch(conf.find_ctimeL).date())
        self.cTimeREdit.setDate(QDateTime.fromSecsSinceEpoch(conf.find_ctimeR).date())
        self.urlLineEdit.setText(conf.find_solved)
        self.textLineEdit.setText(conf.find_text)
        self.solvedCheckBox.setCheckState(BOOL2CHECKSTATE[conf.find_solved])
        return super().show()

    def done(self, arg__1: int) -> None:
        if arg__1:
            self.save()
            self.refresh()
        return super().done(arg__1)

    def refresh(self):
        if not conf.tasks_dir:
            logger.error("Please specify Tasks directory!")
            return
        self.founds = []
        logger.info(f"Depth-first-search Tasks from [{conf.tasks_dir}] with pruning...")
        # tasks = list(load_all_tasks_rec(conf.tasks_dir))
        # logger.info(f"Indexing total {len(tasks)} Tasks...")
        # generate_index(tasks)
        def substr_uncase(sub: str, tot: str):
            sub = "".join(sub.split()).lower()
            tot = "".join(tot.split()).lower()
            return sub in tot
        total = 0
        for task in load_all_tasks_rec(conf.tasks_dir):
            total += 1
            ok = T
            if conf.find_group:
                ok &= substr_uncase(conf.find_group, task.group)
            if conf.find_name:
                ok &= substr_uncase(conf.find_name, task.name)
            if conf.find_url:
                ok &= substr_uncase(conf.find_url, task.url)
            if conf.find_tags:
                ok &= conf.find_tags & task.tags > 0
            if conf.find_solved:
                ok &= conf.find_solved == task.solved
            if self.ctime.isChecked():
                ok &= conf.find_ctimeL <= task.ctime <= conf.find_ctimeR
            if not ok:
                continue
            if conf.find_text:
                ok &= substr_uncase(conf.find_text, open(task.solver).read())  # TODO
            if ok:
                self.founds.append(task)
        logger.info(f"Found {len(self.founds)} matched tasks of total {total}.")
        self.found_tasks_signal.emit(self.founds)


    def save(self):
        conf.find_group = self.grouplineEdit.text()
        conf.find_url = self.urlLineEdit.text()
        conf.find_name = self.nameLineEdit.text()
        conf.find_tags = self.tagsComboBox.currentIndex()
        conf.find_ctimeL = self.cTimeLEdit.dateTime().toSecsSinceEpoch()
        conf.find_ctimeR = self.cTimeREdit.dateTime().toSecsSinceEpoch()
        conf.find_solved = CHECKSTATE2BOOL[self.solvedCheckBox.checkState()]
        conf.find_text = self.textLineEdit.text()


CHECKSTATE2BOOL = {
    Qt.CheckState.Unchecked: F,
    Qt.CheckState.Checked: T,
    Qt.CheckState.PartiallyChecked: None,
}

BOOL2CHECKSTATE = {
    F: Qt.CheckState.Unchecked,
    T: Qt.CheckState.Checked,
    None: Qt.CheckState.PartiallyChecked,
}
