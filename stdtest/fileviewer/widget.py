from PySide6.QtCore import QRect, QRectF, QSizeF
from PySide6.QtGui import QPainter, QTextDocument
from stdtest import *
from .fileviewer_ui import Ui_FileViewer
from .textfinder.textfinder import TextFinder

class TextDocument(QTextDocument):
    
    def set_file(self, file: File):
        self.file = file
        self.setPlainText(file.readAll())

    def blockCount(self) -> int:
        return super().blockCount()
    
    def lineCount(self) -> int:
        return super().lineCount()
    
    def size(self) -> QSizeF:
        ret = super().size()
        print("tSize: ", ret)
        return ret

    def pageSize(self) -> QSizeF:
        ret = super().pageSize()
        print("pSize: ", ret)
        return ret
    
    def drawContents(self, painter: QPainter, rect: QRectF | QRect) -> None:
        return super().drawContents(painter, rect)
    
class TextLayout(QAbstractTextDocumentLayout):
    def __init__(self, doc: QTextDocument) -> None:
        super().__init__(doc)

    def documentSize(self) -> QSizeF:
        return super().documentSize()
    