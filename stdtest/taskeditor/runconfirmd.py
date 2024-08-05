from stdtest import *
from .runconfirmd_ui import Ui_RunConfirmD


class RunConfirmD(QDialog, Ui_RunConfirmD):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setModal(T)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        self.cpuBox.setSuffix(" milliseconds")
        self.cpuBox.setRange(1, 1000 * 3600)
        self.memBox.setSuffix(" megabytes")
        self.memBox.setRange(1, 1024 * 1000)

    def set_task(self, task: Task):
        self.task = task
        from PySide6.QtSvgWidgets import QSvgWidget
        
        self.view = QSvgWidget(get_svgfile(self.task.test_input_type, self.task.test_answer_type), self)
        self.view.renderer().setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)
        self.verticalLayout_2.insertWidget(1, self.view)

#         self.view.set_htmlbody(
#             f"""
# <div style="display: flex;
#     align-items: center;
#     justify-content: center;     
#     height: 100%;"
# >
#     <pre class="dot">{html.escape(DOT[(self.task.test_input_type, self.task.test_answer_type)])}</pre>
# </div>
# """
#         )

        self.radioButton.setChecked(conf.build_debug)
        self.cpuBox.setValue(self.task.cpu_limit)
        self.memBox.setValue(self.task.mem_limit)

    def done(self, arg__1: int) -> None:
        if arg__1:
            conf.build_debug = self.radioButton.isChecked()
            self.cpuBox.setValue(self.task.cpu_limit)
            self.memBox.setValue(self.task.mem_limit)
            self.task.cpu_limit = self.cpuBox.value()
            self.task.mem_limit = self.memBox.value()
        return super().done(arg__1)
