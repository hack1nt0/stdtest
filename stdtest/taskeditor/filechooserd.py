from stdtest import *
from .languageeditord import LanguageEditorD
from .templateeditord import TemplateEditorD
from .filechooser_ui import Ui_FileChooserD

class FileChooserD(QDialog, Ui_FileChooserD):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setModal(T)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        self.textEdit.setTabStopDistance(
            self.textEdit.fontMetrics().horizontalAdvance(" " * 4)
        )
        self.textEdit.setReadOnly(T)

        def pickfile():
            d = QFileDialog(self)
            d.setWindowModality(Qt.WindowModality.WindowModal)
            d.setDirectory(os.getcwd())
            d.setFileMode(QFileDialog.FileMode.ExistingFile)
            d.setWindowTitle("Pick file")
            if d.exec():
                path = d.selectedFiles()[0]
                self.set_file(path)
        self.filepushButton.clicked.connect(pickfile)

        self.status.setStyleSheet("color: red")

        def apply_template():
            d = TemplateEditorD(self)
            d.set_file(self.file)
            d.exec()
        self.applytemplate.clicked.connect(apply_template)
        def edit_commands():
            d = LanguageEditorD(self)
            d.set_file(self.file)
            d.exec()
        self.editcommands.clicked.connect(edit_commands)

        self.applytemplate.setEnabled(F)
        self.editcommands.setEnabled(F)
    
    @property
    def file(self):
        return self.filelineEdit.text().strip()

    def set_task(self, task: Task, filekey: str):
        self.setWindowTitle(filekey)
        self.task = task
        self.filekey = filekey
        self.set_file(getattr(task, filekey))
    
    def set_file(self, file: str):
        if not file:
            return
        self.applytemplate.setEnabled(T)
        self.editcommands.setEnabled(T)
        file = os.path.abspath(file)
        if not file.startswith(self.task.path):
            self.status.setText(f"[{file}] not starts with [{self.task.path}]!")
            return
        self.watcher = QFileSystemWatcher([file], self)
        self.watcher.fileChanged.connect(self.file_changed)
        file = os.path.relpath(file, self.task.path)
        self.filelineEdit.setText(file)
        self.textEdit.setPlainText(open(file).read())
    
    def file_changed(self, v: str):
        self.textEdit.setPlainText(open(v).read())
        self.status.setText(f"Updated @ {datetime.now().isoformat()}")
    
    def done(self, arg__1: int) -> None:
        if arg__1:
            if not self.file:
                self.status.setText("Empty filename!")
                return
            setattr(self.task, self.filekey, self.file)
            save_task_to_json(self.task)
        return super().done(arg__1)