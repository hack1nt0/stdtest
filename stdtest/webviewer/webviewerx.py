import html.parser
from stdtest import *
import glob
from .webviewer_ui import Ui_WebViewer


class WebViewerX(QWidget, Ui_WebViewer):
    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.progressBar.setRange(0, 100)
        self.html = ""
        self.view.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.menu = QMenu(self)
        self.menu.addAction("Debug", self.debug_html)
        self.view.customContextMenuRequested.connect(lambda v: self.menu.popup(QCursor().pos()))
        # self.webEngineView.customContextMenuRequested.connect(lambda: print("HI"))
        self.view.loadProgress.connect(self.progressBar.setValue)

    def set_htmlbody(self, body: str):
        html = io.StringIO()
        html.write(r"""
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
  <script>
    MathJax = {
      tex: {
        inlineMath: [['$', '$']],
        displayMath: [['$$', '$$']],
        processEscapes: true
      }
    };
  </script>
  <script src="https://unpkg.com/d3@5.16.0/dist/d3.min.js"></script>
  <script src="https://unpkg.com/@hpcc-js/wasm@0.3.11/dist/index.min.js"></script>
  <script src="https://unpkg.com/d3-graphviz@3.1.0/build/d3-graphviz.min.js"></script>
  <script>
    function d3ize(elem) {
      var par = elem.parentElement;
      d3.select(par).graphviz().renderDot(elem.innerText);
      d3.select(elem).style('display', 'none');
    }
    window.onload = function() {
      var dotelems = document.getElementsByClassName("dot");
      console.log(dotelems)
      for (let elem of dotelems) {
        d3ize(elem);
      }
    }
  </script>
<style>
  svg {
    height: auto;
    width: 100%;
  }
</style>
</head>
<body style="text-align: center;">

""")
        html.write(body)
        html.write("\n</body>\n</html>")
        html.seek(0)
        self.html = html.read()
        self.view.setHtml(self.html) #TODO

    def set_url(self, url: str):
        self.view.load(url)

    def debug_html(self):
        from .webviewerxd import WebViewerXD
        d = WebViewerXD(self)
        d.show()
