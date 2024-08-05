from stdtest import *
from .languageeditord_ui import Ui_LanguageEditorD

class LanguageEditorD(QDialog, Ui_LanguageEditorD):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setModal(T)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.setWindowTitle(f"Commands")

        def langmodechanged(v: int):
            self.debug.setVisible(not v)
            self.release.setVisible(not v)
        self.checkBox.stateChanged.connect(langmodechanged)

    def set_file(self, file: str):
        self.file = file
        self.language = conf.language(file)
        if self.language:
            self.checkBox.setChecked(self.language.interpreted)
            self.debug.setText(self.language.debug)
            self.release.setText(self.language.release)
            self.execute.setText(self.language.run)

    def done(self, arg__1: int) -> None:
        if arg__1:
            _, suffix = os.path.splitext(self.file)
            lang = conf.languages.get(suffix, {})
            lang["interpreted"] = self.checkBox.isChecked()
            lang["debug"] = self.debug.text()
            lang["release"] = self.release.text()
            lang["run"] = self.execute.text()
            conf.languages[suffix] = lang
        return super().done(arg__1)