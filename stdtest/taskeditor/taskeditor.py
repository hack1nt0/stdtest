from stdtest import *
from .filechooserd import FileChooserD
from .arxivconfirmd import ArxivConfirmD
from .taskeditorw_ui import Ui_TaskEditor


class TaskEditor(QWidget, Ui_TaskEditor):
    def __init__(self, parent: QWidget=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        # self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        self.filechoosers = {
            "solver": self.solver,
            "generator": self.generator,
            "comparator": self.comparator,
            "ichecker": self.ichecker,
        }

        self.textedits = {
            "test_input": self.input,
            "test_output": self.output,
        }

        self.allwidgets = {}
        self.allwidgets.update(self.filechoosers)
        self.allwidgets.update(self.textedits)
        
        self.inputTypes.addItem(TT.MANUAL.value)
        self.inputTypes.addItem(TT.GENERATOR.value)
        self.inputTypes.addItem(TT.UNKNOWN.value)
        self.answerTypes.addItem(TT.MANUAL.value)
        self.answerTypes.addItem(TT.COMPARATOR.value)
        self.answerTypes.addItem(TT.ICHECKER.value)
        self.answerTypes.addItem(TT.UNKNOWN.value)
        self.inputTypes.currentTextChanged.connect(self.test_type_changed)
        self.answerTypes.currentTextChanged.connect(self.test_type_changed)
        self.test_type_changed(TT.MANUAL.value)
        # self.tagsComboBox.addItems(conf.tags)

        for file, widget in self.filechoosers.items():
            widget.clicked.connect(self.choose_file(file))
        # self.arxivButton.clicked.connect(self.arxiv_task)
        # self.arxivButton.setIcon(QIcon(paths.img("check-mark.png")))
        # self.arxivButton.clicked.connect(self.arxiv_task)

    def set_task(self, task: Task):
        if task is None:
            return
        self.task = task
        
        for file, widget in self.filechoosers.items():
            widget.setText(getattr(self.task, file))

        for file, widget in self.textedits.items():
            widget.setPlainText(getattr(self.task, file))

        self.inputTypes.setCurrentText(self.task.test_input_type.value)
        self.answerTypes.setCurrentText(self.task.test_answer_type.value)
    
    def choose_file(self, filekey: str):
        def f():
            d = FileChooserD(self)
            d.set_file(self.task, filekey)
            d.exec()
        return f

    def arxiv_task(self):
        d = ArxivConfirmD(self)
        d.set_task(self.task)
        d.exec()

    def save_task(self):
        self.task.test_input_type = TT(self.inputTypes.currentText())
        self.task.test_answer_type = TT(self.answerTypes.currentText())
        for file, widget in self.textedits.items():
            setattr(self.task, file, widget.toPlainText())
        save_task_to_json(self.task)
        
    def test_type_changed(self, v: str):
        inputType = TT(self.inputTypes.currentText())
        answerType = TT(self.answerTypes.currentText())
        for widget in self.allwidgets.values():
            widget.setVisible(F)
        shows = ["solver"]
        match inputType:
            case TT.MANUAL:
                shows += ["test_input"]
            case TT.GENERATOR:
                shows += ["generator"]
        match answerType:
            case TT.MANUAL:
                shows += ["test_output"]
            case TT.COMPARATOR:
                shows += ["comparator"]
            case TT.ICHECKER:
                shows += ["ichecker"]
                # self.gviewer.set_dot(DOT.IC.value)
        for k in shows:
            self.allwidgets[k].setVisible(T)
        # self.resize(self.minimumSize())


