from stdtest import *
from .doceditor_ui import Ui_DocEditor

class DocEditor(QDialog, Ui_DocEditor):
    def __init__(self, parent: QWidget=None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.tagsComboBox.addItems(conf.tags)
        self.saveButton.clicked.connect(self.save)
        self.saveButton.setShortcut("Ctrl+S")

    
    def set_task(self, task: Task):
        self.task = task
        self.nameLineEdit.setText(self.task.name)
        self.urlLineEdit.setText(self.task.url)
        self.tagsComboBox.setCurrentIndex(self.task.tags)
        self.checkBox.setChecked(self.task.solved)
        # from bs4 import BeautifulSoup
        # parsed_html = BeautifulSoup(open("index.html").read())
        # self.textEdit.setPlainText(parsed_html.body.text)
        self.textEdit.setPlainText(self.task.doc)
    
    def save(self):
        self.task.name = self.nameLineEdit.text()
        self.task.url = self.urlLineEdit.text()
        self.task.tags = self.tagsComboBox.currentIndex()
        self.task.solved = self.checkBox.isChecked()
        self.task.doc = self.textEdit.toPlainText()

        body = f"""
            <h3><a href="{self.task.url}">{self.task.name}</a></h3>
            <h6>{self.task.ctime_str()}</h6>
            {self.task.doc}
        """
        self.view.set_htmlbody(body)

        taskhtml = "index.html"
        with open(taskhtml, "w") as w:
            w.write(self.view.html)
