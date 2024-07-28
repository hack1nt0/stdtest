import html.parser
from stdtest import *
import glob
from .webviewerxd_ui import Ui_WebViewerXD


class WebViewerXD(QDialog, Ui_WebViewerXD):
    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        

        self.view.set_url("http://localhost:7777/")
