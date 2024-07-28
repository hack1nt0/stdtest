from stdtest import *
from .inputbox_ui import Ui_InputBox

class InputBox(QDialog, Ui_InputBox):

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.textEdit.setFont(QFont(*conf.font))
        self.textEdit.setTabStopDistance(
            self.textEdit.fontMetrics().horizontalAdvance(" " * 4)
        )
        self.textEdit.setWordWrapMode(QTextOption.WrapMode.NoWrap)
        self.textEdit.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)

    @property
    def input(self) -> str:
        return self.textEdit.toPlainText()
    