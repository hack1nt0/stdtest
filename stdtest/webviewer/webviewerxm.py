import html.parser

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from stdtest import *
import glob
from .webviewerxm_ui import Ui_WebViewerXM


class WebViewerXM(QMainWindow, Ui_WebViewerXM):
    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
    
    def home(self):
        self.view.set_url("http://localhost:7777/")
        self.show()
