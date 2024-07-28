import json
from stdtest import *


class Listener(BaseHTTPRequestHandler, QObject):

    def do_PUT(self):
        dat = self.rfile.read(int(self.headers["content-length"]))
        dat = json.loads(dat)
        print(json.dumps(dat, indent=4))
        task = load_task_from_json(dat['path'])
        windows["app"].run_task_signal.emit(task)

    def do_POST(self):
        dat = self.rfile.read(int(self.headers["content-length"]))
        windows["app"].new_task_signal.emit(json.loads(dat))
