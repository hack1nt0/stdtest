from PySide6.QtCore import QEvent, QObject, QTimerEvent, Qt
from PySide6.QtGui import QResizeEvent, QWheelEvent
from PySide6.QtWidgets import QWidget
from stdtest import *
import math
import mmap
import copy
from .hugefileviewer_ui import Ui_HugeFileViewer


@dataclasses.dataclass
class Pointer:
    row: int = 0
    col: int = 0

    def __eq__(self, o: object) -> bool:
        return self.row == o.row and self.col == o.col
    
    def __ne__(self, o: object) -> bool:
        return not self == o
    
    def __lt__(self, o: object) -> bool:
        return self.row < o.row if self.row != o.row else self.col < o.col

class Model:

    def __init__(self, file: File) -> None:
        self.reader = open(file.path, "rb")
        self.readOffset = 0

    def __len__(self) -> int:
        return os.path.getsize(self.reader.fileno())

    def read(self, offset: int, size: int) -> bytes:
        self.reader.seek(offset)
        return self.reader.read(size)

class Mode(enum.Enum):
    TailF = "Tail -F"
    Normal = "Normal"
    Selection = "Visual"

class Highlighter(QSyntaxHighlighter):

    def __init__(self, document: QTextDocument):
        super().__init__(document)
        self.re_format = {
            Qt.GlobalColor.blue: r"(test #|input|answer|actual|verdict|chat)",
            Qt.GlobalColor.green: r"(ok|passed)",
            Qt.GlobalColor.red: r"(fail|error)",
            Qt.GlobalColor.yellow: r"(warn|unknown|terminate)",
        }
        self.find_pattern: str = ""
        self.find_fmt = QTextCharFormat()
        self.find_fmt.setBackground(BLUE)
        self.find_fmt.setForeground(YELLOW)

    def set_pattern(self, pat: str):
        self.find_pattern = pat
        self.rehighlight()

    def highlightBlock(self, text: str) -> None:
        # print(f'[[{self.currentBlock().blockNumber()}]] - [[{text}]]')
        # if not self.pattern or not text:
        #     return
        if self.find_pattern:
            for m in re.finditer(self.find_pattern, text, re.RegexFlag.IGNORECASE):
                s, c = m.start(), m.end() - m.start()
                self.setFormat(s, c, self.find_fmt)
        else:
            for color, regex in self.re_format.items():
                for m in re.finditer(regex, text, re.RegexFlag.IGNORECASE):
                    s, c = m.start(), m.end() - m.start()
                    self.setFormat(s, c, color)
        # super().highlightBlock(text)

class HugeFileViewer(QWidget, Ui_HugeFileViewer):
    change_page_signal: Signal = Signal(int)
    clear_signal: Signal = Signal()

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.textEdit.setReadOnly(T)
        self.textEdit.setUndoRedoEnabled(F)
        self.textEdit.setWordWrapMode(QTextOption.WrapMode.NoWrap)
        self.textEdit.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
        self.textEdit.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByKeyboard
        )

        self.textEdit.setFont(QFont(*conf.font))
        self.textEdit.setTabStopDistance(
            self.textEdit.fontMetrics().horizontalAdvance(" " * 4)
        )
        self.lineHeight = self.textEdit.fontMetrics().height() - 0  # TODO


        self.textEdit.installEventFilter(self)
        self.textEdit.viewport().installEventFilter(self)
        self.verticalScrollBar.installEventFilter(self)

        self.textEdit.textCursor().movePosition(QTextCursor.MoveOperation.NextCharacter)

        def set_lineOffset(v):
            if self.mode == Mode.TailF:
                self.mode = Mode.Normal
            self.firstLine = v
            self.ptr.row = v
            self.ptr.col = 0
            self.refresh()

        self.verticalScrollBar.valueChanged.connect(set_lineOffset)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.readTimer = None

        # self.textEdit.selectionChanged.connect(self.selection_changed)
        # self.textEdit.cursorPositionChanged.connect

        self.highlighter = Highlighter(self.textEdit.document())

        self.clear_signal.connect(self.clear)

        self.clear()

    @property
    def lines(self) -> int:
        return len(self.lineOffsets) - 1

    @property
    def lastLine(self) -> int:
        return self.firstLine + self.pageLines - 1

    def line(self, idx: int) -> str:
        return self.model.read(self.lineOffsets[idx], self.lineOffsets[idx + 1] - self.lineOffsets[idx]).decode()

    def lineLen(self, idx: int) -> int:
        return self.lineOffsets[idx + 1] - self.lineOffsets[idx] if self.lines else 0
    
    def copy(self) -> str:
        sPtr = self.selectionStartPtr
        tPtr = self.ptr
        if self.ptr < self.selectionStartPtr:
            sPtr = self.ptr
            tPtr = self.selectionStartPtr
        sRow, sCol, tRow, tCol = sPtr.row, sPtr.col, tPtr.row, tPtr.col
        assert sPtr.row < tPtr.row or sPtr.row == tPtr.row and sPtr.col <= tPtr.col
        offset = self.lineOffsets[sRow] + sCol
        size = self.lineOffsets[tRow] - offset + tCol
        text = self.model.read(offset, size).decode()
        QGuiApplication.clipboard().setText(text)

    @property
    def maxFirstLine(self) -> int:
        return max(0, self.lines - self.pageLines)

    def clear(self):
        if self.readTimer:
            self.killTimer(self.readTimer)
        # logger_file.clear()
        self.model = Model(self.file)
        self.byteOffset = 0
        self.lastLinePartial = F
        self.mode: Mode = Mode.TailF
        self.ptr = Pointer()
        self.selectionStartPtr = None  # TODO
        self.lineOffsets = [0]
        # self.pageLines = 1
        self.firstLine = 0
        self.findOffset = 0
        self.reading = F
        self.highlighter.find_pattern = None
        self.readTimer = self.startTimer(100)
        # self.textEdit.setTextInteractionFlags(
        #     Qt.TextInteractionFlag.TextSelectableByKeyboard
        # )
    def set_html(self, string: str):
        self.clear()
        self.textEdit.setHtml(string)
        # self.textEdit.setTextInteractionFlags(
        #     Qt.TextInteractionFlag.TextBrowserInteraction
        # )

    def refresh(self):
        if not self.lines:
            return
        if self.mode == Mode.TailF:
            self.ptr.row = self.lines - 1
            self.ptr.col = self.lineLen(self.ptr.row)
            self.firstLine = self.maxFirstLine
            self.selectionStartPtr = None
        else:
            self.ptr.row = max(0, min(self.ptr.row, self.lines - 1))
            self.ptr.col = max(0, min(self.ptr.col, self.lineLen(self.ptr.row) - 1)) #TODO
            self.firstLine = max(0, min(self.firstLine, self.lines - 1))
            if self.ptr.row < self.firstLine:
                self.firstLine = self.ptr.row
            elif self.lastLine < self.ptr.row:
                self.firstLine = self.ptr.row - self.pageLines + 1

        self.verticalScrollBar.blockSignals(T)
        self.verticalScrollBar.setRange(0, self.lines - self.pageLines)
        self.verticalScrollBar.setValue(self.firstLine)
        self.verticalScrollBar.blockSignals(F)

        offset = self.lineOffsets[self.firstLine]
        size = self.lineOffsets[min(self.firstLine + self.pageLines, self.lines)] - offset
        if size:
            content = self.model.read(offset, size).decode(errors="replace")
            self.textEdit.setPlainText(content)

        def update_cursor(tc: QTextCursor, rowDelta: int, colDelta: int, select: bool = F):
            moveMode = (
                QTextCursor.MoveMode.KeepAnchor
                if select
                else QTextCursor.MoveMode.MoveAnchor
            )
            if rowDelta > 0:
                tc.movePosition(QTextCursor.MoveOperation.NextBlock, moveMode, n=rowDelta)
            if colDelta > 0:
                tc.movePosition(QTextCursor.MoveOperation.NextCharacter, moveMode, n=colDelta)

        def update_cursor_row(tc: QTextCursor, rowDelta: int, select: bool = F):
            moveMode = (
                QTextCursor.MoveMode.KeepAnchor
                if select
                else QTextCursor.MoveMode.MoveAnchor
            )
            tc.movePosition(QTextCursor.MoveOperation.Next, moveMode, n=rowDelta)
            

        if self.selectionStartPtr and self.selectionStartPtr != self.ptr:
            sPtr = self.selectionStartPtr
            tPtr = self.ptr
            if self.ptr < self.selectionStartPtr:
                sPtr = self.ptr
                tPtr = self.selectionStartPtr
            sRow, sCol, tRow, tCol = sPtr.row - self.firstLine, sPtr.col, tPtr.row - self.firstLine, tPtr.col
            if sRow < 0:
                sRow, sCol = 0, 0
            elif self.pageLines <= tRow:
                tRow, tCol = self.pageLines - 1, self.lineLen(self.lastLine)
            tc = self.textEdit.textCursor()
            tc.movePosition(QTextCursor.MoveOperation.Start)
            update_cursor(tc, sRow, sCol, select=F)
            if tRow == sRow:
                update_cursor(tc, 0, tCol - sCol, select=T)
            else:
                update_cursor(tc, tRow - sRow, tCol, select=T)
            self.textEdit.setTextCursor(tc)
        else:
            tc = self.textEdit.textCursor()
            tc.movePosition(QTextCursor.MoveOperation.Start)
            update_cursor(tc, self.ptr.row - self.firstLine, self.ptr.col)
            self.textEdit.setTextCursor(tc)

        self.statusLine.setText(
            # f"<span style='color:blue'>Mode[</span>"
            # f"{self.mode}"
            # f"<span style='color:blue'>] </span>"
            f"<span style='color:blue'>Row/Total = </span>"
            f"{self.ptr.row + 1}/{self.lines}"
            f"<span style='color:blue'>\tColumn = </span>"
            f"{self.ptr.col}"
            # f"<span style='color:blue'>Page Lines = </span>"
            # f"{self.pageLines}"
        )

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        # print(watched, event)
        if (
            watched
            in (
                self.textEdit.viewport(),
                self.textEdit,
                self.verticalScrollBar,
            )
            and event.type() == QEvent.Type.Wheel
        ):
            event: QWheelEvent
            y = event.angleDelta().y()
            if self.mode == Mode.TailF:
                self.mode = Mode.Normal
            self.firstLine += -1 if y > 0 else 1
            self.ptr.row += -1 if y > 0 else 1
            self.refresh()
            return T
        if watched is self.textEdit:
            if event.type() == QEvent.Type.KeyPress:
                e: QKeyEvent = event
                # if e.modifiers() == Qt.KeyboardModifier.ShiftModifier:
                if e.key() == Qt.Key.Key_Escape:
                    if self.selectionStartPtr:
                        self.selectionStartPtr = None
                        self.refresh()
                    elif self.highlighter.find_pattern:
                        self.highlighter.find_pattern = None
                        self.refresh()
                        
                    if self.mode == Mode.Selection:
                        self.mode = Mode.Normal
                        self.selectionStartPtr = None
                        self.refresh()
                    elif self.mode == Mode.Normal:
                        # disable fidn highlight
                        self.mode = Mode.TailF
                        self.refresh()
                    return T
                elif e.key() == Qt.Key.Key_V:
                    if self.selectionStartPtr is None:
                        self.mode = Mode.Selection
                        self.selectionStartPtr = Pointer(self.ptr.row, self.ptr.col)
                        self.refresh()
                    return T
                elif e.key() == Qt.Key.Key_PageUp:
                    if self.mode == Mode.TailF:
                        self.mode = Mode.Normal
                    self.ptr.row -= self.pageLines
                    self.firstLine -= self.pageLines
                    self.refresh()
                    return T
                elif e.key() == Qt.Key.Key_PageDown:
                    if self.mode == Mode.TailF:
                        self.mode = Mode.Normal
                    self.ptr.row += self.pageLines
                    self.firstLine += self.pageLines
                    self.refresh()
                    return T
                elif e.key() in (Qt.Key.Key_Up, Qt.Key.Key_K):
                    print(e)
                    if e.modifiers() == Qt.KeyboardModifier.ShiftModifier:
                        if self.selectionStartPtr is None:
                            self.selectionStartPtr = copy.copy(self.ptr)
                    if self.mode == Mode.TailF:
                        self.mode = Mode.Normal
                    self.ptr.row -= 1
                    self.refresh()
                    return T
                elif e.key() in (Qt.Key.Key_Down, Qt.Key.Key_J):
                    if self.mode == Mode.TailF:
                        self.mode = Mode.Normal
                    self.ptr.row += 1
                    self.refresh()
                    return T
                elif e.key() in (Qt.Key.Key_Left, Qt.Key.Key_H):
                    if self.mode == Mode.TailF:
                        self.mode = Mode.Normal
                    if 0 < self.ptr.col:
                        self.ptr.col -= 1
                        self.refresh()
                    return T
                elif e.key() in (Qt.Key.Key_Right, Qt.Key.Key_L):
                    if self.mode == Mode.TailF:
                        self.mode = Mode.Normal
                    if self.ptr.col < self.lineLen(self.ptr.row):
                        self.ptr.col += 1
                        self.refresh()
                    return T
                elif e.key() == Qt.Key.Key_G and e.modifiers() == Qt.KeyboardModifier.NoModifier:
                    if self.mode == Mode.TailF:
                        self.mode = Mode.Normal
                    self.ptr.row = 0
                    self.ptr.col = 0
                    self.firstLine = 0
                    self.refresh()
                    return T
                elif e.key() == Qt.Key.Key_G and e.modifiers() == Qt.KeyboardModifier.ShiftModifier:
                    if self.mode == Mode.TailF:
                        self.mode = Mode.Normal
                    self.ptr.row = self.lines - 1
                    self.ptr.col = self.lineLen(self.ptr.row)
                    self.firstLine = self.maxFirstLine
                    self.refresh()
                    return T
                elif e.key() == Qt.Key.Key_C and e.modifiers() == Qt.KeyboardModifier.ControlModifier:
                    if self.mode == Mode.Selection:
                        self.copy()
                        #TODO
                    return T
                elif e.key() == Qt.Key.Key_Slash:
                    if self.mode == Mode.TailF:
                        self.mode = Mode.Normal
                    self.find_box()
                    return T
                elif e.key() == Qt.Key.Key_N and e.modifiers() == Qt.KeyboardModifier.NoModifier:
                    if self.mode == Mode.TailF:
                        self.mode = Mode.Normal
                    self.find_next(+1)
                    return T
                elif e.key() == Qt.Key.Key_N and e.modifiers() == Qt.KeyboardModifier.ShiftModifier:
                    if self.mode == Mode.TailF:
                        self.mode = Mode.Normal
                    self.find_next(-1)
                    return T
            # elif event.type() == QEvent.Type.MouseButtonPress:
            #     tc = self.textEdit.cursorForPosition(event.pos())
            #     self.ptr.row = tc.blockNumber() + self.firstLine
            #     self.ptr.col = tc.positionInBlock()
            #     return T
        # print(watched, event)
        return F

    def read(self, v: int = None):
        if self.reading:
            return
        self.reading = T
        if self.byteOffset < len(self.model):
            # if self.mmap is not None:
            #     self.mmap.close()
            # self.mmap = mmap.mmap(self.fileno, 0, prot=mmap.PROT_READ)
            # self.mmap.seek(self.byteOffset)
            buf = self.model.read(self.byteOffset, conf.bytes_per_read)
            while buf:
                idx = buf.find(b"\n")
                if idx < 0:
                    self.byteOffset += len(buf)
                    if self.lastLinePartial:
                        self.lineOffsets[-1] = self.byteOffset
                    else:
                        self.lineOffsets.append(self.byteOffset)
                        self.lastLinePartial = T
                    break
                self.lastLinePartial = F
                Len = idx + 1
                self.byteOffset += Len
                self.lineOffsets.append(self.byteOffset)
                buf = buf[Len:]
            self.mode = Mode.TailF
            self.refresh()

        self.reading = F

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        height = self.textEdit.height()
        self.pageLines = math.floor(height / self.lineHeight)
        self.refresh()


    def timerEvent(self, event: QTimerEvent) -> None:
        if event.timerId() == self.readTimer:
            self.read()
        return super().timerEvent(event)
    
    def find_box(self):
        pattern_str, ok = QInputDialog.getText(
            self,
            "Find",
            "Regular Expr (Case Insensitive): ",
            text=self.highlighter.find_pattern,
            # flags=Qt.WindowType.Popup,
        )
        if not ok:
            return
        if pattern_str != self.highlighter.find_pattern:
            self.highlighter.set_pattern(pattern_str)
            self.findOffset = 0
        self.find_next()
        # doc = QTextDocument(self)
        # doc.find
        # for firstLine, page in self.pages_itr():
        #     pass
    
    def find_next(self, dir: int=1):
        if not self.highlighter.find_pattern or not self.lines:
            return
        startLine = self.findOffset
        while T:
            line = self.line(self.findOffset)
            ret = re.search(self.highlighter.find_pattern, line, re.RegexFlag.IGNORECASE)
            if ret:
                if self.findOffset < self.firstLine or self.lastLine < self.findOffset:
                    self.firstLine = self.lastLine
                self.ptr.row = self.findOffset
                self.ptr.col = ret.start()
                self.refresh()
            self.findOffset = (self.findOffset + dir) % self.lines
            if self.findOffset == startLine or ret:
                break
            
    

