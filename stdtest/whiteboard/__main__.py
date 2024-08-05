from stdtest import *
from .gview import GView
from .whiteboard import WhiteBoard

if __name__ == "__main__":
    app = QApplication()
    w = WhiteBoard()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec())