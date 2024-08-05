from stdtest import *
from .gview import Mode
from .whiteboard_ui import Ui_WhiteBoard


class WhiteBoard(QWidget, Ui_WhiteBoard):
    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.label.setText("""Ctrl + Move: draw
Shift + Move: Erase
LClick + Move: drag
Wheel: Zoom""")

        # self.view.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        # self.menu = QMenu(self)
        # self.menu.addAction("Clear", self.clear)
        # self.view.customContextMenuRequested.connect(lambda v: self.menu.popup(QCursor().pos()))

        self.color = Qt.GlobalColor.blue
        self.colorButton.clicked.connect(self.pick_color)

        self.clearButton.clicked.connect(self.clear)

        self.saveButton.clicked.connect(self.view.save_svg)

    def clear(self):
        self.view.clear()
    
    def pick_color(self):
        d = QColorDialog(self)
        d.setCurrentColor(self.color)
        def set_color(color: QColor):
            self.view.set_color(color)
            self.color = color
        d.colorSelected.connect(set_color)
        d.exec()
    
