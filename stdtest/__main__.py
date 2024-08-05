from stdtest import *
from stdtest.main.main import Main
from stdtest.listener import Listener


class App(QApplication):
    new_task_signal: Signal = Signal(dict)
    run_task_signal: Signal = Signal(Task)

    # def notify(self, obj: QObject, e: QEvent) -> bool:
    #     if (
    #         e.type() == QEvent.Type.KeyPress
    #         and e.key() == Qt.Key.Key_Tab
    #         and isinstance(obj, TerminalPanel)
    #     ):
    #         obj.keyPressEvent(e)
    #         return T
    #     try:
    #         return super().notify(obj, e)
    #     except BaseException as e:
    #         logger.exception(e)
    #         pass
    #     finally:
    #         return F


if __name__ == "__main__":
    # app = App(["--webEngineArgs", "--remote-debugging-port=7777"])
    # app = QApplication()
    app = App()
    windows["app"] = app
    app.setStyleSheet(open(paths.data("stdtest.css")).read())

    # debugwebviewer = WebViewerXM()
    # debugwebviewer.hide()
    # windows["debugwebviewer"] = debugwebviewer

    # app.setStyle("fusion")

    main = Main()
    # app.paletteChanged.connect(lambda v: windows["terminal"].set_color(v))  # TODO
    main.show()

    if not conf.tasks_dir:
        main.testsuite.pick_tasksdir()

    
    app.new_task_signal.connect(main.testsuite.new_task)
    server = HTTPServer(("localhost", 27121), Listener)
    global_threadpool.submit(server.serve_forever)
    logger.info("Listener on")


    returncode = app.exec()
    conf.save()
    server.shutdown()
    sys.exit(returncode)
