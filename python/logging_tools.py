import os
import datetime
from pathlib import Path
import inspect


def init(log_dir: str = ""):
    date = datetime.date.today()
    dateFormat = date.strftime("%d-%b-%Y")
    log_name = f"DATA_{dateFormat}.log"
    if log_dir == "":
        log_dir = os.path.join(os.getcwd(), "logs")
    log_path = os.path.join(log_dir, log_name)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    if not os.path.exists(log_path):
        timestamp = dateTime_now()
        with open(log_path, 'w') as f:
            f.write(f"[INIT][{timestamp}]\n")
    return log_path


def dateTime_now() -> str:
    date = datetime.datetime.now()
    dateFormat = date.strftime("%d-%b-%Y %H:%M:%S")
    return dateFormat


def info(data: str):
    log_path = init()
    # file name:
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    filename = os.path.basename(module.__file__)  # returns filename where function is called
    # function name:
    caller_name = inspect.stack()[1][3]
    # timestamp:
    timestamp = dateTime_now()
    #
    with open(log_path, "a") as file:
        file.write(f"[{filename}][{caller_name}][INFO][{timestamp}] {data}\n")


def warning(data: str):
    log_path = init()
    # file name:
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    filename = os.path.basename(module.__file__)  # returns filename where function is called
    # function name:
    caller_name = inspect.stack()[1][3]
    # timestamp:
    timestamp = dateTime_now()
    #
    with open(log_path, "a") as file:
        file.write(f"[{filename}][{caller_name}][WARNING][{timestamp}] {data}\n")


def debug(data: str):
    log_path = init()
    # file name:
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    filename = os.path.basename(module.__file__)  # returns filename where function is called
    # function name:
    caller_name = inspect.stack()[1][3]
    # timestamp:
    timestamp = dateTime_now()
    #
    with open(log_path, "a") as file:
        file.write(f"[{filename}][{caller_name}][DEBUG][{timestamp}] {data}\n")


def error(data):
    log_path = init()
    # file name:
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    filename = os.path.basename(module.__file__)  # returns filename where function is called
    # function name:
    caller_name = inspect.stack()[1][3]
    # timestamp:
    timestamp = dateTime_now()
    #
    with open(log_path, "a") as file:
        file.write(f"[{filename}][{caller_name}][ERROR][{timestamp}] {data}\n")
