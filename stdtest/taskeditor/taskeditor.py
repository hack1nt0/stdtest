from stdtest import *
from .filechooserd import FileChooserD
from .testeditord import TestEditorD
from .taskeditorw_ui import Ui_TaskEditor


class TaskEditor(QWidget, Ui_TaskEditor):
    def __init__(self, parent: QWidget=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        # self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        def select_solver():
            d = FileChooserD(self)
            d.set_task(self.task, "solver")
            d.exec()
        self.solver.clicked.connect(select_solver)
        def edit_tests():
            d = TestEditorD(self)
            d.set_task(self.task)
            d.exec()
        self.tests.clicked.connect(edit_tests)

    def set_task(self, task: Task):
        self.task = task
    