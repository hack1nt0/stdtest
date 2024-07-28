from stdtest import *
from .widget import TextDocument, TextLayout
from .hugefileviewer import HugeFileViewer


if __name__ == "__main__":
    app = QApplication()
    # d = TextDocument(app)
    # d.set_file(File(os.path.expanduser("~/out")))
    # w = QTextEdit()
    # w.setDocument(d)
    # l = TextLayout(d)
    # w.document().setDocumentLayout(l)
    # w.show()
    # assert w.document() == d

    # d = QTextDocument()
    # d.setPlainText(File(os.path.expanduser("~/out")).read())
    # p = QTextCursor(d)
    
    # ww = QPlainTextEdit()
    # slider = ww.verticalScrollBar()
    
    # slider.valueChanged.connect(lambda v: print(f"{v} in [{slider.minimum()}:{slider.maximum()}:{slider.singleStep()}:{slider.pageStep()}]"))
    # ww.setPlainText(File(os.path.expanduser("~/out")).read())
    # ww.show()

    hw = HugeFileViewer()
    hw.show()
    hw.set_file(os.path.expanduser("/Users/dy/Downloads/simplewiki-20170820-pages-meta-current.xml.bz2/simplewiki-20170820-pages-meta-current.xml"))
    # hw.set_file(os.path.expanduser("/Users/dy/out2"))
    sys.exit(app.exec())
