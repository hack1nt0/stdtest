
from stdtest import *
from .gviewerx import GViewerX

if __name__ == "__main__":
    app = QApplication()
    # with open(paths.data("cchelper.css"), "r") as r:
    #     app.setStyleSheet(r.read())
    w = GViewerX(None)
    w.show()
    sys.exit(app.exec())