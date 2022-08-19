import os
import datetime
from pathlib import Path
import inspect


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


# called from individual functions. no need to call directly
def init(log_dir: str = ""):
    date = datetime.date.today()
    dateFormat = date.strftime("%d-%b-%Y")
    log_name = f"DATA_{dateFormat}.log"
    if log_dir == "":
        log_dir = os.path.join(os.getcwd(), "logs")
    log_path = os.path.join(log_dir, log_name)
    #
    if not os.path.exists(log_dir):  # if directory doesn't exist
        os.makedirs(log_dir)
    if not os.path.exists(log_path):
        timestamp = dateTime_now()
        with open(log_path, 'w') as f:
            f.write(f"[INIT][{timestamp}]\n")
    #
    return log_path


# run at end of script to archive log file
def archive_log_file():
    log_path = init()
    if not os.path.exists(log_path):
        print(f"No log file found: {log_path}")
        return
    # rename log file
    date = datetime.datetime.now()
    dateTimeFormat = date.strftime("%d-%b-%Y_%H:%M:%S")
    new_log_file = f"DATA_{dateTimeFormat}.archive.log"
    new_log_file_path = os.path.join(os.path.dirname(log_path), new_log_file)
    os.rename(log_path, new_log_file_path)
    print(f"log file archived: {new_log_file_path}")


def dateTime_now() -> str:
    date = datetime.datetime.now()
    dateFormat = date.strftime("%d-%b-%Y %H:%M:%S")
    return dateFormat
