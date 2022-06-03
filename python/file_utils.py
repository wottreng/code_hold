import os
import datetime
import json
from system_utils import *

'''
module for reading and writing data
Version 1.4
written by Mark Wottreng
'''


def write_string_to_file(data: str, path: str = os.getcwd(), filename: str = "data.txt", method: str = "w") -> bool:
    if check_for_folder(path):
        with open(os.path.join(path, filename), method) as file:
            file.write(f"{data}\n")
        return True
    else:
        print("path not found: ", path)
        return False


def write_list_to_file(data: list, path: str = os.getcwd(), filename: str = "dataList.txt", method: str = "w") -> bool:
    if check_for_folder(path):
        with open(os.path.join(path, filename), method) as file:
            for line in data:
                file.write(f"{line}\n")
        return True
    else:
        print("path not found: ", path)
        return False


def write_dict_to_file(data: dict, path: str = os.getcwd(), filename: str = "dataList.txt", method: str = "w") -> bool:
    if check_for_folder(path):
        with open(os.path.join(path, filename), method) as file:
            for key, value in data.items():
                file.write(f"{key}:{value},")
            file.write("\n")
        return True
    else:
        print("path not found: ", path)
        return False


def write_dict_to_json_file(data: dict, path: str = os.getcwd(), filename: str = "data.json",
                            method: str = "w") -> bool:
    with open(os.path.join(path, filename), method) as json_file:
        json.dump(data, json_file)
    return True


def read_dict_from_json_file(path: str = os.getcwd(), filename: str = "data.json") -> dict:
    if check_if_file_exists(os.path.join(path, filename)):
        with open(os.path.join(path, filename), "r") as json_file:
            json_data = json.load(json_file)
        return json_data
    else:
        print(f"[!] file not found: {filename}")
        return {}


def read_list_from_file(path: str = os.getcwd(), filename: str = "dataList.txt") -> list:
    dataList: list = []
    if check_if_file_exists(os.path.join(path, filename)):
        with open(os.path.join(path, filename), "r") as file:
            data: list = file.readlines()
        for line in data:
            dataList.append(line.strip())
        return dataList
    else:
        print(f"[!] file not found: {filename}")
        return []


# write string to debug file
def debug_log(data: str, mode: str = "a", log_location=os.getcwd()) -> bool:
    if check_for_folder(log_location):
        date = datetime.datetime.now()
        dateFormat = date.strftime("%d-%b-%Y %H:%M:%S")
        filename = "debug_log.txt"
        with open(os.path.join(log_location, filename), mode) as log:
            log.write(f"{dateFormat} >< {data}\n")
        return True
    else:
        print("path not found: ", log_location)
        return False
