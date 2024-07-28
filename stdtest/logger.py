import logging, os
import traceback
import sys
from datetime import datetime
from .entity import File
import stdtest.paths as paths

__all__ = [
    "logger_file",
    "logger",
    "log",
]

logger_file = os.path.expanduser("~/.stdtest/stdtest.log")
log = open(logger_file, "w")
sys.stdout = log
sys.stderr = log

class Logger:
    def __init__(self) -> None:
        self.logger = logging.getLogger("CcHelper")
        self.logger.setLevel(logging.DEBUG)
        file_h = logging.FileHandler(logger_file)
        file_h.setFormatter(
            logging.Formatter("%(message)s")
        )
        file_h.setLevel(logging.DEBUG)
        self.logger.addHandler(file_h)

    def set_level(self, v):
        self.logger.setLevel(v)

    def error(self, msg: str):
        
        self.logger.error(msg)

    def info(self, msg: str, timeout=-1):
        msg = str(msg)
        self.logger.info(msg)

    def warn(self, msg: str, timeout=-1):
        msg = str(msg)
        self.logger.warn(msg)

    def exception(self, e: BaseException):
        self.logger.exception(e)

    def debug(self, msg: str):
        msg = str(msg)
        self.logger.debug(msg)

logger = Logger()

def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    logger.exception(tb)

sys.excepthook = excepthook
