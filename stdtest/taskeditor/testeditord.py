from stdtest import *
from .filechooserd import FileChooserD
from .testeditord_ui import Ui_TestEditorD


class TestEditorD(QDialog, Ui_TestEditorD):
    def __init__(self, parent: QWidget=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        # self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        self.filechoosers = {
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
        self.inputTypes.currentTextChanged.connect(self.test_inputtype_changed)
        self.answerTypes.currentTextChanged.connect(self.test_answertype_changed)

        for file, widget in self.filechoosers.items():
            widget.clicked.connect(self.choose_file(file))

    def set_task(self, task: Task):
        if task is None:
            return
        self.task = task
        
        for file, widget in self.filechoosers.items():
            widget.setText(getattr(self.task, file))

        for file, widget in self.textedits.items():
            widget.setPlainText(getattr(self.task, file))

        self.inputTypes.blockSignals(T)
        self.inputTypes.setCurrentText(self.task.test_input_type.value)
        self.inputTypes.blockSignals(F)
        self.test_inputtype_changed(self.inputType.value)
    
    def choose_file(self, filekey: str):
        def f():
            d = FileChooserD(self)
            d.set_task(self.task, filekey)
            d.exec()
        return f
    
    @property
    def inputType(self) -> TT:
        return TT(self.inputTypes.currentText())

    @property
    def answerType(self) -> TT:
        return TT(self.answerTypes.currentText())

    def test_inputtype_changed(self, v: str):
        self.answerTypes.blockSignals(T)
        match self.inputType:
            case TT.MANUAL:
                self.answerTypes.clear()
                self.answerTypes.addItem(TT.MANUAL.value)
                self.answerTypes.addItem(TT.COMPARATOR.value)
                self.answerTypes.addItem(TT.ICHECKER.value)
                self.answerTypes.addItem(TT.UNKNOWN.value)
            case TT.GENERATOR:
                self.answerTypes.clear()
                self.answerTypes.addItem(TT.COMPARATOR.value)
                self.answerTypes.addItem(TT.ICHECKER.value)
                self.answerTypes.addItem(TT.UNKNOWN.value)
        self.answerTypes.setCurrentText(self.task.test_answer_type.value)
        self.answerTypes.blockSignals(F)
        self.test_answertype_changed(self.answerType.value)

    def test_answertype_changed(self, v: str):
        for widget in self.allwidgets.values():
            widget.setVisible(F)
        shows = []
        match self.inputType:
            case TT.MANUAL:
                shows += ["test_input"]
            case TT.GENERATOR:
                shows += ["generator"]
        match self.answerType:
            case TT.MANUAL:
                shows += ["test_output"]
            case TT.COMPARATOR:
                shows += ["comparator"]
            case TT.ICHECKER:
                shows += ["ichecker"]
        for k in shows:
            self.allwidgets[k].setVisible(T)

    def done(self, arg__1: int) -> None:
        if arg__1:
            self.task.test_input_type = TT(self.inputType)
            self.task.test_answer_type = TT(self.answerType)
            for file, widget in self.textedits.items():
                setattr(self.task, file, widget.toPlainText())
            save_task_to_json(self.task)
        return super().done(arg__1)