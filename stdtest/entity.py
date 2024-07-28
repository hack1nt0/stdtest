import dataclasses
from dataclasses import dataclass, field
import time
import enum
import os

# from .db import db
from typing import List, Tuple, Dict, Any
import json
import glob
import pickle
import shutil
from pathlib import Path
import itertools
import math
import io
from concurrent.futures import ThreadPoolExecutor
from PySide6.QtGui import QFont

T, F = True, False
import stdtest.paths as paths

import sys
import pathlib
import typing
import shlex
from datetime import datetime

_WIN = sys.platform == "win32"


__all__ = [
    "_WIN",
    "Language",
    "build_debug",
    "TS",
    "TT",
    "DOT",
    "Task",
    "load_task_from_json",
    "load_all_tasks",
    "load_all_tasks_rec",
    "save_task_to_json",
    "TaskCondition",
    "Test",
    "Verdict",
    "VS",
    "CT",
    "IT",
    "AT",
    "File",
    "TokenFile",
    "conf",
    "paths",
]

build_debug: bool = T
run_inshell: bool = F


@dataclasses.dataclass
class Language:
    name: str = ""
    filename: str = ""
    template: List[str] = None
    interpreted: bool = False
    debug: str = ""
    release: str = ""
    run: str = ""


class Configuration:
    def __init__(self) -> None:
        self.prefer_solver = "solver.cpp"
        self.tasks_dir = os.path.expanduser("~")
        self.find_group = ""
        self.find_name = ""
        self.find_url = ""
        self.find_tags = 0
        self.find_solved = None
        self.find_ctimeL = 0
        self.find_ctimeR = int(datetime.now().timestamp())
        self.find_text = ""

        self.refresh_rate = 10
        self.languages = {
            ".cpp": {
                "name": "C++",
                "filename": "solver.cpp",
                "interpreted": False,
                "debug": "c++ -I/Users/dy/cc/include -std=c++17 -g -Wall -DDEBUG -fsanitize=address -fsanitize=undefined -o {output} {input}",
                "release": "c++ -I/Users/dy/cc/include -std=c++17 -O2 -o {output} {input}",
                "template": [
                    r"""
#include "debug.h"

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(&cout);

    return 0;
}
""",
                    r"""
#include "debug.h"

void solve(int it) {}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(&cout);
    int n; cin >> n;
    for (int i = 0; i < n; ++i) solve(i);
    return 0;
}
""",
                    r"""
#include "debug.h"

void solve(int it) {}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(&cout);
    for (int it = 0; solve(it); it++);
    return 0;
}
""",
                ],
            },
            ".py": {
                "name": "Python",
                "filename": "solver.py",
                "interpreted": True,
                "run": "python3 -Xfrozen_modules=off {}",
                "template": [
                    r"""
import random
n = int(1e6)
print(n)
for _ in range(n):
    x = random.randint(0, 10)
    y = random.randint(0, 10)
    print(x, y)
""",
                    r"""
import random
n = int(1e6)
print(n)
for _ in range(n):
    x = random.randint(0, 10)
    y = random.randint(0, 10)
    print(x, y)
""",
                    r"""
import random
n = int(1e6)
print(n)
for _ in range(n):
    x = random.randint(0, 10)
    y = random.randint(0, 10)
    print(x, y)
""",
                ],
            },
        }
        self.tags = [
            "Graph Theory",
            "Greedy",
            "Math",
            "Heuristic",
            "Dynamic Programming",
            "Data Structure",
            "Binary Search",
            "Backtracking",
        ]
        self.bytes_per_page = 100000
        self.bytes_per_cell = 1000
        self.bytes_per_read = 1024 * 1024
        self.rows_per_page = 100
        self.log_level = "DEBUG"
        self.exe_dump_delay = 1
        self.exe_warm_delay = 2
        self.font = (["PT Mono", "JetBrains Mono", "Courier New"], 12)
        self.host = "localhost"
        self.port = 22
        self.username = "dy"
        self.password = "6666"
        self.edit_file_limit = int(5e6)
        self.parallel = 1
        self.build_debug = T

    def language(self, file: str) -> Language:
        prefix, suffix = os.path.splitext(file)
        return Language(**self.languages[suffix]) if suffix in self.languages else None

    def compile_cmd(self, file: str) -> str:
        # TODO -it : ERR the input device is not a TTY
        # ret = f"docker exec dev bash compile{self.suffix}.sh /code/tasks/{self.taskname} {self.path} {self.executable} {1 if conf.build_debug else 0}"
        lang = self.language(file)
        if not lang:
            return None
        ret = None
        prefix, suffix = os.path.splitext(file)
        ret = lang.debug if conf.build_debug else lang.release
        ret = ret.format(input=file, output=f"{prefix}.exe")
        if _WIN:
            ret = f"wsl {ret}"
        return self.format_cmd(ret)

    def execute_cmd(self, file) -> str:
        lang = self.language(file)
        if not lang:
            return None
        ret = None
        prefix, suffix = os.path.splitext(file)
        if suffix not in conf.languages:
            return
        ret = lang.run.format(file) if lang.interpreted else f"./{prefix}.exe"
        if _WIN:
            ret = f"wsl {ret}"
        return self.format_cmd(ret)

    def format_cmd(self, cmd: str) -> str | List[str] | None:
        if not cmd:
            return
        import shlex

        return shlex.split(cmd)  # TODO

    def save(self):
        open(CONFFILE, "w").write(json.dumps(self, indent=4, cls=JsonEncoder))


CONFFILE = os.path.expanduser("~/.stdtest/config.json")
conf = Configuration()
if os.path.exists(CONFFILE):
    jsondat = json.loads(open(CONFFILE).read())
    for k, v in jsondat.items():
        if hasattr(conf, k):
            setattr(conf, k, v)


class JsonEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        return o.__dict__


class CT(enum.Enum):
    TBT = "Token By Token"
    CBC = "Char By Char"


@dataclasses.dataclass
class File:
    path: str

    def create(self):
        if not os.path.exists(self.path):
            root = os.path.dirname(os.path.abspath(self.path))
            os.makedirs(root, exist_ok=T)
            with open(self.path, "w") as w:
                pass
        return self

    def readAll(self) -> str:
        return open(self.path, "r").read()

    def readlines(self) -> List[str]:
        return open(self.path, "r").readlines()

    def write(self, o):
        if isinstance(o, File):
            with open(self.path, "w") as w:
                for line in open(o):
                    w.write(line)
        else:
            assert isinstance(o, str)
            with open(self.path, "w") as w:
                w.write(o)

    def __iadd__(self, value: bytes | str):
        if value is None:
            return self
        if type(value) != bytes:  # TODO
            value = str(value).encode()
        with open(self.path, "ab", buffering=0) as w:
            w.write(value)
            w.write(b"\n")
        return self

    def appendLine(self, value: bytes | str):
        if value is None:
            return self
        if type(value) != bytes:  # TODO
            value = str(value).encode()
        with open(self.path, "ab") as w:
            w.write(value)
            w.write(b"\n")
            w.flush()
        return self

    def clear(self):
        with open(self.path, "wb") as w:
            w.truncate(0)
            w.seek(
                0
            )  # Important, else you will have weird \x00 appended at the start of the file.

    # tail
    def summary(self, MAX_CS=100):
        with open(self.path, "rb", buffering=0) as r:
            L = r.seek(0, 2)
            L1 = (MAX_CS + 1) // 2
            L2 = MAX_CS // 2
            R1 = (0, min(L, L1))
            R2 = (max(R1[1], L - L2), L)
            L1 = R1[1] - R1[0]
            L2 = R2[1] - R2[0]
            r.seek(0, 0)
            S1 = r.read(L1)
            r.seek(-L2, 2)
            S2 = r.read(L2)
            M = "... ..." if R1[1] < R2[0] else ""
            return M.join((S1.decode(), S2.decode()))

    def tail(self, MAX_CS=1000) -> str:
        with open(self.path, "rb", buffering=0) as r:
            r
            L = r.seek(0, 2)
            L2 = min(MAX_CS, L)
            r.seek(-L2, 2)
            S = r.read(L2)
            # H = "..." if L2 < L else ""
            return S.decode(errors="ignore")  # TODO may cause decode error

    def head(self, MAX_CS=1000) -> str:
        with open(self.path, "rb", buffering=0) as r:
            L = r.seek(0, 2)
            r.seek(0)
            s = r.read(MAX_CS)
        s = s.decode(errors="ignore")
        if MAX_CS < L:
            s += "\n... ..."
        return s

    def __eq__(self, othr) -> bool:
        if type(othr) is not File:
            return F
        if len(self) != len(othr):
            return F
        with (
            open(self.path, "rb", buffering=0) as r1,
            open(othr.path, "rb", buffering=0) as r2,
        ):
            while T:
                c1 = r1.read(conf.bytes_per_read)
                c2 = r2.read(conf.bytes_per_read)
                if c1 != c2:
                    return F
                if len(c1) == 0:
                    return T

    def __ne__(self, othr) -> bool:
        return not (self == othr)

    def __len__(self) -> int:
        return os.path.getsize(self.path)

    def __bool__(self) -> bool:
        return os.path.exists(self.path) and len(self) > 0

    @property
    def length(self) -> int:
        return len(self)

    @property
    def mtime(self) -> int:
        return round(os.path.getmtime(self.path))


class TokenFile(File):

    def __init__(self, obj: File) -> None:
        super().__init__(obj.path)

    def __eq__(self, othr) -> bool:
        if type(othr) is not TokenFile:
            return F

        def tokens(stream):
            for line in stream:
                for tk in line.split():
                    yield tk

        with (
            open(self.path, "r") as a,
            open(othr.path, "r") as b,
        ):
            for atoken, btoken in itertools.zip_longest(tokens(a), tokens(b)):
                ret = F
                if atoken and btoken:
                    try:
                        ret = abs(float(atoken) - float(btoken)) < 1e-6
                    except ValueError:
                        ret = atoken == btoken
                if not ret:
                    return F
        return T


class VS(enum.Enum):
    TERMINATE = "Terminated"
    SKIP = "Skipped"
    SUCCESS = "Successful"
    FAIL = "Failed"


class IT(enum.Enum):
    MANUAL = "Manual"
    GENERATOR = "Generator"


class AT(enum.Enum):
    UNKNOWN = "Unknown"
    MANUAL = "Manual"
    JURGER = "Jurger"
    # INTERACTIVE_JURGER = "Interactive-J"


@dataclasses.dataclass
class Test:
    id: int = None
    input: str = ""
    answer: str = ""
    status: VS = VS.SUCCESS
    checked: bool = True

    def remove(self):
        try:
            shutil.rmtree(os.path.dirname(self.input.path))
        except:
            pass


@dataclasses.dataclass
class Verdict:
    flow_bytes: int = 0
    cpu: int = 0
    mem: int = 0
    text: str = ""

    @property
    def progress(self) -> int:
        try:
            return self.flow_bytes * 100 // len(self.input)
        except:
            return 100


class TS(enum.Enum):
    SOLVED = "Solved"
    UNSURE = "Unsure"
    UNSOLVED = "unSolved"


class TT(enum.Enum):
    MANUAL = "Manual"
    GENERATOR = "Generator"
    COMPARATOR = "Comparator"
    ICHECKER = "Interactive Checker"
    UNKNOWN = "Unknown"
    FILE = "File"

    MI = "Manual Input"
    RI_RA = "Raw Input/Raw Answer"
    G_C = "Generator/Comparator"
    BF = "Brute Force"
    IC = "Interactive Checker"


DOT = {
    (
        TT.MANUAL,
        TT.MANUAL,
    ): """
digraph {
	label="Test Input & Test Answer";
	rankdir=LR

	testinput [label=<Test Input> shape=box]
	testanswer [label=<Test Answer> shape=box]
	solver [label=<Solver>]
	checker [label=<Token-based Checker>]
    testinput -> solver -> checker
    testanswer -> checker
}""",
    (
        TT.MANUAL,
        TT.UNKNOWN,
    ): """
digraph {
	label="Test Input Only";
	rankdir=LR

	testinput [label=<Test Input> shape=box]
	solver [label=<Solver>]
    testinput -> solver 
}""",
    (
        TT.GENERATOR,
        TT.COMPARATOR,
    ): """
digraph {
	label="Generator & Comparator";
	rankdir=LR
    
	testinput [label=<Test Input> shape=box]
	checker [label=<Token-based Checker>]
    Generator -> testinput
    testinput -> Comparator -> checker
    testinput -> Solver -> checker
}""",
    (
        TT.GENERATOR,
        TT.UNKNOWN,
    ): """
digraph {
	label="Generator only (Bruteforce)";
	rankdir=LR
    
	testinput [label=<Test Input> shape=box]
    Generator -> testinput -> Solver
}""",
    (
        TT.MANUAL,
        TT.ICHECKER,
    ): """
digraph {
	label="Test Input & Interactive Checker";
	rankdir=LR
	
	testinput [label=<Test Input> shape=box]
	solver [label=<Solver>]
    ichecker [label=<Interactive Checker>]
    testinput -> ichecker [label=<1>]
    ichecker -> solver [label=<2>]
    solver -> ichecker [label=<3>]
}""",
    (
        TT.GENERATOR,
        TT.ICHECKER,
    ): """
digraph {
	label="Generator & Interactive Checker";
	rankdir=LR
    
	generator [label=<Generator>]
	testinput [label=<Test Input> shape=box]
	solver [label=<Solver>]
    ichecker [label=<Interactive Checker>]
    generator -> testinput [label=<1>]
    testinput -> ichecker [label=<2>]
    ichecker -> solver [label=<3>]
    solver -> ichecker [label=<4>]
}""",
}


@dataclass
class Task:
    path: str = ""
    group: str = ""
    name: str = ""

    # test_type: TT = TT.RI_RA
    test_input_type: TT = TT.MANUAL
    test_answer_type: TT = TT.MANUAL

    solver: str = ""
    generator: str = ""
    comparator: str = ""
    ichecker: str = ""
    _combined_files: dict = field(default_factory=lambda: {})

    cpu_limit: int = 1000
    mem_limit: int = 128
    cpu: int = 0
    mem: int = 0
    pipe: int = 0

    solved: bool = F

    tags: int = 0
    url: str = ""
    doc: str = ""

    ctime: int = field(default_factory=lambda: int(time.time()))

    manual_input: str = "input.txt"
    test_input: str = ""
    test_output: str = ""

    def remove(self):
        shutil.rmtree(self.path)

    def ctime_str(self):
        return datetime.fromtimestamp(self.ctime).isoformat()

    def href(self):
        return os.path.relpath(self.path, conf.tasks_dir)

    def getTags(self):
        return [
            conf.tags[idx] for idx in range(len(conf.tags)) if (self.tags >> idx & 1)
        ]


def load_task_from_json(dir: str) -> Task | None:
    meta = os.path.join(dir, "meta.json")
    if os.path.exists(meta):
        with open(meta, "r") as r:
            dat = json.load(r)
            task = Task()
            for k, v in dat.items():
                if hasattr(task, k):
                    if k in [
                        "test_input_type",
                        "test_answer_type",
                    ]:
                        setattr(task, k, TT(v))
                    else:
                        setattr(task, k, v)
        task.path = dir
        return task
    # else:
    #     task = Task(name=os.path.basename(dir))


def save_task_to_json(task: Task):
    os.makedirs(task.path, exist_ok=T)
    meta = os.path.join(task.path, "meta.json")
    dat = {
        "group": task.group,
        "name": task.name,
        "test_input_type": task.test_input_type.value,
        "test_answer_type": task.test_answer_type.value,
        "solver": task.solver,
        "generator": task.generator,
        "comparator": task.comparator,
        "ichecker": task.ichecker,
        "cpu_limit": task.cpu_limit,
        "mem_limit": task.mem_limit,
        "solved": task.solved,
        "tags": task.tags,
        "url": task.url,
        "doc": task.doc,
        "ctime": task.ctime,
        "test_input": task.test_input,
        "test_output": task.test_output,
    }
    with open(meta, "w") as w:
        json.dump(dat, w, indent=4)


def load_all_tasks(root: str):
    for droot, dns, fns in os.walk(root):
        for dn in dns:
            task = load_task_from_json(os.path.join(droot, dn))
            if task:
                yield task
        break


def load_all_tasks_rec(root: str):
    for droot, dns, fns in os.walk(root):
        task = load_task_from_json(droot)
        if task:
            yield task
            continue


import re


@dataclasses.dataclass
class TaskCondition:
    url: str = None
    name: str = None
    tags: int = 0
    solver: re.Pattern = None
    ctimeL: int = None
    ctimeR: int = None
    status: TS = None
