from stdtest import *
import glob
from .taskfinder_ui import Ui_TaskFinder


class TaskFinderD(QDialog, Ui_TaskFinder):
    find_task_signal: Signal = Signal(TaskCondition)
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
        tasks = list(load_all_tasks_rec(conf.tasks_dir))
        logger.info(f"Indexing total {len(tasks)} Tasks...")
        self.generate_index(tasks)
        def substr_uncase(sub: str, tot: str):
            sub = "".join(sub.split()).lower()
            tot = "".join(tot.split()).lower()
            return sub in tot
        for task in tasks:
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
        logger.info(f"Found {len(self.founds)} matched Tasks.")
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

    def generate_index(self, tasks: List[Task]):
        tasks.sort(key=lambda task: task.ctime, reverse=T)
        indexhtml = os.path.join(conf.tasks_dir, "index.html")
        with open(indexhtml, "w") as w:
            w.write(
                """
<html>
<style>
table, th, td {
  border:1px solid black;
}
</style>
<head>
  <meta charset="utf-8">
  <style>
    table { 
        margin-left: auto;
        margin-right: auto;
    }
    .center-col {
        text-align: center; 
        vertical-align: middle;
    }
    </style>
</head>
  <body style="text-align: center;">
""")
            w.write(f"<p>Total: {len(tasks)}</p>")
            w.write("""
    <table>
      <tr>
        <th>C.Time</th>
        <th>Group</th>
        <th>Prob. Name</th>
        <th>Tags</th>
      </tr>
"""
            )
            for task in tasks:
                w.write("<tr>")
                w.write(f'<td>{task.ctime_str()}</td>')
                w.write(f'<td class="center-col">{task.group}</td>')
                w.write(f'<td><a href="{task.href()}">{task.name}</a></td>')
                w.write('<td class="center-col">')
                if not task.solved:
                    w.write("""<div style="color: red">Unsolved</div>""")
                for tag in task.getTags():
                    w.write(f'<div>{tag}</div>')
                w.write("</td>")
                w.write("</tr>\n")
            w.write(
                """
    </table>
  </body>
</html> 
"""
            )

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
