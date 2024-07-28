from stdtest import *
from .taskeditor_ui import Ui_TaskEditorD

class TaskEditorD(QDialog, Ui_TaskEditorD):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setModal(T)
        # self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

    def set_task(self, task: Task):
        self.task = task
        self.testParamsEditor.set_task(task)
        self.taskTagsEditor.set_task(task)
        self.show()

    def done(self, arg__1: int) -> None:
        if arg__1:
            self.testParamsEditor.save()
            self.taskTagsEditor.save()
            save_task_to_json(self.task)
        return super().done(arg__1)