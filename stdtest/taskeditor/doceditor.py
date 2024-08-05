from stdtest import *
from .doceditor_ui import Ui_DocEditor

class DocEditor(QDialog, Ui_DocEditor):
    def __init__(self, parent: QWidget=None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.tagsComboBox.addItems(conf.tags)
        self.saveButton.clicked.connect(self.save)
        self.saveButton.setShortcut("Ctrl+S")
        self.generateindexButton.clicked.connect(generate_index)

        self.footer.setTextFormat(Qt.TextFormat.RichText)
        
        dot = html.escape("""<div style="display: flex; 
        align-items: center; 
        justify-content: center;     
        height: 100%;">
    <pre class="dot">DOT SOURCE</pre>
</div>""")
        self.footer.setText(f"""
    <table style="border:1px solid black;">
      <tr>
        <th>Type</th>
        <th>Html</th>
      </tr>
      <tr>
        <td>Math</td>
        <td>{html.escape("$/$$")}</td>
    </tr>
      <tr>
        <td>Graphviz.dot</td>
        <td><pre>{dot}</pre></td>
    </tr>
    </table>
""")
    
    def set_task(self, task: Task):
        self.task = task
        self.nameLineEdit.setText(self.task.name)
        self.groupLineEdit.setText(self.task.group)
        self.tagsComboBox.setCurrentIndex(self.task.tags)
        self.checkBox.setChecked(self.task.solved)
        # from bs4 import BeautifulSoup
        # parsed_html = BeautifulSoup(open("index.html").read())
        # self.textEdit.setPlainText(parsed_html.body.text)
        self.textEdit.setPlainText(self.task.doc)
    
    def save(self):
        self.task.name = self.nameLineEdit.text()
        self.task.group = self.groupLineEdit.text()
        self.task.tags = self.tagsComboBox.currentIndex()
        self.task.solved = self.checkBox.isChecked()
        self.task.doc = self.textEdit.toPlainText()

        body = f"""
            <h3><a href="{self.task.url}">{self.task.name}</a></h3>
            <h6>{self.task.ctime_str()}</h6>
            {self.task.doc}
        """
        # self.view.set_htmlbody(body)

        taskhtml = "index.html"
        with open(taskhtml, "w") as w:
            w.write(generate_html(body))
        
        QDesktopServices.openUrl(QUrl.fromLocalFile(os.path.realpath(taskhtml)))

def generate_html(body: str) -> str:
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
        return html.read()

def generate_index():
    tasks = list(load_all_tasks_rec(conf.tasks_dir))
    tasks.sort(key=lambda task: task.ctime, reverse=T)
    indexhtml = os.path.join(conf.tasks_dir, "index.html")
    with open(indexhtml, "w") as w:
        w.write(
            """
<html>
<style>
table, th, td {
  border:1px solid black;
}
</style>
<head>
  <meta charset="utf-8">
  <style>
    table { 
        margin-left: auto;
        margin-right: auto;
    }
    .center-col {
        text-align: center; 
        vertical-align: middle;
    }
    </style>
</head>
  <body style="text-align: center;">
""")
        w.write(f"<p>Total: {len(tasks)}</p>")
        w.write("""
    <table>
      <tr>
        <th>C.Time</th>
        <th>Group</th>
        <th>Prob. Name</th>
        <th>Tags</th>
      </tr>
"""
            )
        for task in tasks:
            w.write("<tr>")
            w.write(f'<td>{task.ctime_str()}</td>')
            w.write(f'<td class="center-col">{task.group}</td>')
            w.write(f'<td><a href="{task.href()}">{task.name}</a></td>')
            w.write('<td class="center-col">')
            if not task.solved:
                w.write("""<div style="color: red">Unsolved</div>""")
            for tag in task.getTags():
                w.write(f'<div>{tag}</div>')
            w.write("</td>")
            w.write("</tr>\n")
        w.write(
                """
    </table>
  </body>
</html> 
"""
            )