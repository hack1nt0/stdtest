from stdtest import *
from .templateeditord_ui import Ui_TemplateEditorD

class TemplateEditorD(QDialog, Ui_TemplateEditorD):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setModal(T)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.textEdit.setTabStopDistance(
            self.textEdit.fontMetrics().horizontalAdvance(" " * 4)
        )
        self.setWindowTitle(f"Templates")

        self.radios = [self.radioButton, self.radioButton_2, self.radioButton_3]
        for idx, radio in enumerate(self.radios):
            radio.toggled.connect(lambda v, idx=idx: self.template_changed(idx))

    def set_file(self, file: str):
        self.file = file
        self.language = conf.language(file)
        if self.language:
            self.setWindowTitle(f"Template of [{self.language.name}]")
            self.template_changed(0)
    
    def template_changed(self, idx: int):
        self.radios[idx].setChecked(T)
        self.templateid = idx
        self.textEdit.setPlainText(self.language.template[idx])
    
    def done(self, arg__1: int) -> None:
        if arg__1:
            _, suffix = os.path.splitext(self.file)
            lang = conf.languages.get(suffix, {})
            temp = self.textEdit.toPlainText()
            lang["template"][self.templateid] = temp
            conf.languages[suffix] = lang
            open(self.file, "w").write(temp)
        return super().done(arg__1)