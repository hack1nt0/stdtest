from stdtest import *
from .webviewerx import WebViewerX
from stdtest.taskeditor.arxivconfirmd import ArxivConfirmD

if __name__ == "__main__":
    app = QApplication(['', '--no-sandbox'])
    # w = WebViewerX()
    w = ArxivConfirmD()
    w.resize(640, 480)
    cwd = os.path.dirname(os.path.realpath(__file__))
    # w.set_root(os.path.join(cwd, "test.html"))
    w.set_task(load_task_from_json("/Users/dy/gits/cc/D.Cat,FoxandMaximumArraySplit2"))
    w.show()
    sys.exit(app.exec())