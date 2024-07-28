from stdtest import *
from .filechooser_ui import Ui_FileChooserD

class FileChooserD(QDialog, Ui_FileChooserD):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setModal(T)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        self.namelineEdit.editingFinished.connect(self.name_changed)
        def pickfile():
            d = QFileDialog(self)
            d.setWindowModality(Qt.WindowModality.WindowModal)
            # d.setDirectory(os.getcwd())
            d.setFileMode(QFileDialog.FileMode.ExistingFile)
            d.setWindowTitle("Pick file")
            if d.exec():
                path = d.selectedFiles()[0]
                self.namelineEdit.setText(os.path.relpath(path, self.task.path))
        self.namepushButton.clicked.connect(pickfile)

        self.radios = [self.radioButton, self.radioButton_2, self.radioButton_3]
        self.radios[0].setChecked(T)
        self.templateid = 0
        for idx, radio in enumerate(self.radios):
            radio.toggled.connect(lambda v, idx=idx: self.template_changed(idx))
        
        def langmodechanged(v: int):
            self.debug.setVisible(not v)
            self.release.setVisible(not v)
        self.checkBox.stateChanged.connect(langmodechanged)
    
        self.applytemplateButton.clicked.connect(lambda: self.create(force=T))
    

    def set_file(self, task: Task, filekey: str):
        self.setWindowTitle(filekey)
        self.task = task
        self.filekey = filekey
        self.file = getattr(task, filekey)
        self.namelineEdit.setText(self.file)
        self.namelineEdit.editingFinished.emit()

    def name_changed(self):
        self.file = self.namelineEdit.text().strip()
        lang = conf.language(self.file)
        if lang:
            self.radios[0].setChecked(lang.interpreted)
            self.textEdit.setPlainText(lang.template[0])
            self.templateid = 0
            self.checkBox.setChecked(lang.interpreted)
            self.debug.setText(lang.debug)
            self.release.setText(lang.release)
            self.execute.setText(lang.run)
    
    def template_changed(self, idx: int):
        self.templateid = idx
        if not self.file:
            return
        self.textEdit.setPlainText(conf.language(self.file).template[idx])

    def create(self, force: bool=F):
        self.file = self.namelineEdit.text()
        setattr(self.task, self.filekey, self.file)
        if force or not os.path.exists(self.file):
            open(self.file, "w").write(self.textEdit.toPlainText())
        _, suffix = os.path.splitext(self.file)
        lang = conf.languages.get(suffix, {})
        lang["template"][self.templateid] = self.textEdit.toPlainText()
        lang["interpreted"] = self.checkBox.isChecked()
        lang["debug"] = self.debug.text()
        lang["release"] = self.release.text()
        lang["run"] = self.execute.text()
    
    def done(self, arg__1: int) -> None:
        if arg__1:
            if not self.namelineEdit.text().strip():
                return
            self.create()
        return super().done(arg__1)