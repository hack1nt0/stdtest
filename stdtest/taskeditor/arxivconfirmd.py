from stdtest import *
from .arxivconfirmd_ui import Ui_ArxivConfirmD

class ArxivConfirmD(QDialog, Ui_ArxivConfirmD):
    def __init__(self, parent: QWidget=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setModal(T)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        self.tagsComboBox.addItem("*")
        self.tagsComboBox.addItems(conf.tags)
        self.buttonBox.button(QDialogButtonBox.StandardButton.Save).clicked.connect(self.save)
    
    def set_task(self, task: Task):
        self.task = task
        self.nameLineEdit.setText(self.task.name)
        self.urlLineEdit.setText(self.task.url)
        self.tagsComboBox.setCurrentIndex(self.task.tags)
        self.checkBox.setChecked(self.task.solved)
        self.doc.set_task(self.task)
    
    def save(self):
        self.task.name = self.nameLineEdit.text()
        self.task.url = self.urlLineEdit.text()
        self.task.tags = self.tagsComboBox.currentIndex()
        self.task.solved = self.checkBox.isChecked()
        self.doc.save_task()

    def done(self, arg__1: int) -> None:
        return super().done(arg__1)