from functools import cached_property
import os
from stdtest import *


class WebViewer(QtWebEngineWidgets.QWebEngineView):
    def __init__(self, parent=None):
        super().__init__(parent)

    def set_root(self, root: str):
        self.root = root
        self.directory = os.path.dirname(root)
        self.load(QUrl.fromLocalFile(self.root))
        self.page().loadFinished.connect(self.load_finished)

        self.watcher = QFileSystemWatcher([self.root])
        self.watcher.fileChanged.connect(lambda v: self.reload())

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.menu = QMenu(self)
        self.menu
        self.customContextMenuRequested.connect(self.pop_up)

    def load_finished(self):
        for jsfile in self.download_javascripts():
            self.page().runJavaScript(open(jsfile).read())
        logger.info(f"{self.root} loaded sucessfully")

    def download_javascripts(self):
        return [
            os.path.join(self.directory, "mathjax.js"),
            os.path.join(self.directory, "mathjaxconfig.js"),
        ]
    
    def pop_up(self, p: QPoint):
        
