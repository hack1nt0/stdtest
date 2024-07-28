from stdtest import *
from .codeeditordialog_ui import Ui_CodeEditorDialog


class CodeEditorD(QDialog, Ui_CodeEditorDialog):
    saved_signal: Signal = Signal()

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.fa = parent

        self.widget.saved_signal.connect(self.saved_signal.emit)

        self.terminalButton.setShortcut("Ctrl+T")
        self.terminalButton.clicked.connect(self.openInVim)

        self.buttonBox.button(QDialogButtonBox.StandardButton.Ok).clicked.connect(
            lambda: self.done(1)
        )
        self.buttonBox.button(QDialogButtonBox.StandardButton.Cancel).clicked.connect(
            lambda: self.done(0)
        )

    def set_file(self, file: File):
        self.file = file
        self.widget.set_file(file)

    def openInVim(self):
        windows['terminal'].open_file(self.file)
        self.close()

    def done(self, arg__1: int) -> None:
        if arg__1:
            self.widget.save()
        else:
            new = self.widget.textEdit.toPlainText()
            old = (
                open(self.file.path, "r", errors='replace').read()
                if os.path.exists(self.file.path)
                else None
            )
            if new != old:
                d = ConfirmBox(self, "File had changed, save changes ?")
                match d.exec():
                    case ConfirmBox.YES:
                        self.widget.save()
                    case ConfirmBox.NO:
                        pass
                    case ConfirmBox.CANCEL:
                        return
        super().done(arg__1)
