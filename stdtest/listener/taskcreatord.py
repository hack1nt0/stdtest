from stdtest import *
from .taskcreatord_ui import Ui_TaskCreatorD


class TaskCreatorD(QDialog, Ui_TaskCreatorD):

    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setModal(T)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        self.task = Task()

    def set_json(self, jsondict: dict):
        task = Task()
        task.name = jsondict["name"]
        task.group = jsondict["group"]
        task.url = jsondict["url"]
        task.cpu_limit = jsondict["timeLimit"]
        task.mem_limit = jsondict["memoryLimit"]
        if jsondict["interactive"]:
            task.test_input_type = TT.MANUAL
            task.test_answer_type = TT.ICHECKER
        else:
            task.test_input_type = TT.MANUAL
            task.test_answer_type = TT.MANUAL
        inputs, outputs = [], []
        for test in jsondict["tests"]:
            inputs.append(test["input"])
            outputs.append(test["output"])
        task.test_input = "\n".join(inputs)
        task.test_output = "\n".join(outputs)
        
        self.task = task
        self.groupLineEdit.setText(task.group)
        self.nameLineEdit.setText(task.name)
        self.solverLineEdit.setText(conf.prefer_solver)

    def done(self, arg__1: int) -> None:
        if arg__1:
            self.task.group = self.groupLineEdit.text()
            self.task.name = self.nameLineEdit.text()
            self.task.solver = self.solverLineEdit.text()
            conf.prefer_solver = self.solverLineEdit.text()
            if not self.task.name or not conf.tasks_dir or not self.task.solver:
                self.status.setText("All fields should be filled!")
                return
            path = "".join(filter(lambda c: c.isalnum(), self.task.name)).lower()
            self.task.path = os.path.join(conf.tasks_dir, path)

            if os.path.exists(self.task.path):
                logger.info(f"Task [{self.task.name} maybe existed, will stash it")
            os.makedirs(self.task.path, exist_ok=T)

            lang = conf.language(self.task.solver)
            if lang:
                solver = os.path.join(self.task.path, lang.filename)
                if not os.path.exists(solver):
                    open(solver, "w").write(lang.template[0])
            save_task_to_json(self.task)
            logger.error(f"Task [{self.task.name}] created sucessfully in [{self.task.path}]")
            if self.checkBox.isChecked():
                conf.find_group = self.groupLineEdit.text()
        return super().done(arg__1)
