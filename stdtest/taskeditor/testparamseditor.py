from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from stdtest import *
from PySide6.QtSvgWidgets import QSvgWidget, QGraphicsSvgItem
from stdtest.gviewer import GViewer
from .testparamseditor_ui import Ui_TestParamsEditor


class TestParamsEditor(QWidget, Ui_TestParamsEditor):

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        # self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        self.map = {
            "solver": (
                self.solverLabel,
                self.solverlineEdit,
                self.solverButton,
                QMenu(self),
            ),
            "checker": (
                self.checkerLabel,
                self.checkerlineEdit,
                self.checkerButton,
                QMenu(self),
            ),
            "generator": (
                self.generatorLabel,
                self.generatorlineEdit,
                self.generatorButton,
                QMenu(self),
            ),
            "comparator": (
                self.comparatorLabel,
                self.comparatorlineEdit,
                self.comparatorButton,
                QMenu(self),
            ),
            "manual_input": (
                self.fileLabel,
                self.filelineEdit,
                self.fileButton,
                QMenu(self),
            ),
        }
        for k, (label, edit, btn, menu) in self.map.items():
            menu.addAction("Select", lambda k=k, edit=edit: self.select_file(k, edit))
            btn.setMenu(menu)

        for tt in TT:
            self.testTypeComboBox.addItem(tt.value)
        self.testTypeComboBox.currentTextChanged.connect(self.test_type_changed)
        self.testTypeComboBox.setCurrentIndex(1)
        # self.test_type_changed(TT.RI_RA.value)

        self.graphButton.setIcon(QIcon(paths.img("data-analytics.png")))
        self.graphButton.clicked.connect(self.show_graph)


    def set_task(self, task: Task):
        self.task = task
        self.testTypeComboBox.setCurrentText(task.test_type.value)
        for k, (label, edit, btn, menu) in self.map.items():
            try:
                edit.setText(getattr(task, k))
            except:
                edit.setText("")
        self.input.setPlainText(task.test_input)
        self.output.setPlainText(task.test_output)

        self.cpuBox.setValue(self.task.cpu_limit)
        self.memBox.setValue(self.task.mem_limit)

        self.radioButton.setChecked(conf.build_debug)


    def test_type_changed(self, v: str):
        tt = TT(v)
        for label, edit, btn, menu in self.map.values():
            label.setEnabled(F)
            edit.setEnabled(F)
            btn.setEnabled(F)
        self.input.setEnabled(F)
        self.output.setEnabled(F)
        match tt:
            case TT.MI:
                for k in ["manual_input"]:
                    label, edit, btn, menu = self.map[k]
                    label.setEnabled(T)
                    edit.setEnabled(T)
                    btn.setEnabled(T)
            case TT.RI_RA:
                self.input.setEnabled(T)
                self.output.setEnabled(T)
            case TT.G_C:
                for k in ["generator", "comparator"]:
                    label, edit, btn, menu = self.map[k]
                    label.setEnabled(T)
                    edit.setEnabled(T)
                    btn.setEnabled(T)
            case TT.BF:
                for k in ["generator"]:
                    label, edit, btn, menu = self.map[k]
                    label.setEnabled(T)
                    edit.setEnabled(T)
                    btn.setEnabled(T)
            case TT.IC:
                for k in ["generator", "checker"]:
                    label, edit, btn, menu = self.map[k]
                    label.setEnabled(T)
                    edit.setEnabled(T)
                    btn.setEnabled(T)
                

    def select_file(self, k: str, edit: QLineEdit):
        d = QFileDialog(self)
        d.setWindowModality(Qt.WindowModality.WindowModal)
        d.setDirectory(self.task.path)
        d.setFileMode(QFileDialog.FileMode.ExistingFile)
        if d.exec():
            path = os.path.relpath(d.selectedFiles()[0], self.task.path)
            setattr(self.task, k, path)
            edit.setText(path)

    def save(self):
        for k, (label, edit, btn, menu) in self.map.items():
            path = edit.text().strip()
            setattr(self.task, k, path)
        self.task.test_type = TT(self.testTypeComboBox.currentText())
        self.task.test_input = self.input.toPlainText()
        self.task.test_output = self.output.toPlainText()
        self.task.cpu_limit = self.cpuBox.value()
        self.task.mem_limit = self.memBox.value()
        conf.build_debug = self.radioButton.isChecked()

    def show_graph(self):
        d = GraphViewer(self)
        d.set_dot("""
digraph {
	labelloc="t";
	label="Flow Graph";
	bgcolor="transparent";
	rankdir=LR
	node [shape=record ]
	edge []
	
	0 [label=<input>]
	1 [label=<answer>]
	2 [label=<solver>]
	3 [label=<checker>]
	0 -> 3 [label=<1>]
	1 -> 3 [label=<2>]
	2 -> 3 [label=<4>]
	3 -> 2 [label=<3>]
	
} 
                  """)
        d.exec()
        # self.svg.renderer().boundsOnElement()