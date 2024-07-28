from stdtest import *
from .tasktagseditor_ui import Ui_TaskTagsEditor


class TaskTagsEditor(QWidget, Ui_TaskTagsEditor):
    def __init__(self, parent: QWidget=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        # self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

    def set_task(self, task: Task):
        self.task = task
        self.tagsComboBox.addItems(conf.tags)
        self.tagsComboBox.setCurrentIndex(self.task.tags)
        self.urlLineEdit.setText(self.task.url)
        self.docLineEdit.setText(self.task.doc)
        
        # self.statusComboBox.addItems([ts.value for ts in TS])
        # self.statusComboBox.setCurrentText(self.task.status.value)
        self.nameLineEdit.setText(self.task.name)

    def save(self):
        self.task.name = self.nameLineEdit.text().strip()
        self.task.tags = self.tagsComboBox.currentIndex()
        self.task.url = self.urlLineEdit.text().strip()
        self.task.doc = self.docLineEdit.text().strip()
        # self.task.status = TS(self.statusComboBox.currentText())
