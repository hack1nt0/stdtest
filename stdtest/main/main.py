from PySide6.QtGui import QCloseEvent
from stdtest import *
from .main_ui import Ui_MainWindow

class Main(QMainWindow, Ui_MainWindow):

    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

    
    # def set_task(self, task: Task):
    #     self.testsuite.set_task(task)

    # def closeEvent(self, event: QCloseEvent) -> None:
    #     if self.testsuite.task:
    #         self.testsuite.task.save()
    #     return super().closeEvent(event)