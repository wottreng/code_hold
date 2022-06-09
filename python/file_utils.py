'''
module for reading and writing data
Version 1.5
written by Mark Wottreng
'''

import os
import datetime
import json
import ast
from system_utils import *


def write_string_to_file(data: str, path: str, filename: str, method: str = "w") -> bool:
    if not check_for_folder(path):
        print("[ERROR] path not found: ", path)
        return False
    # write data to file
    with open(os.path.join(path, filename), method) as file:
        file.write(f"{data}\n")
    return True


def write_list_to_file(data: list, path: str, filename: str, method: str = "w") -> bool:
    if not check_for_folder(path):
        print("[ERROR] path not found: ", path)
        return False
    # write data to file
    with open(os.path.join(path, filename), method) as file:
        for line in data:
            file.write(f"{line}\n")
    return True


def write_dict_to_file(data: dict, path: str, filename: str, method: str = "w") -> bool:
    if not check_for_folder(path):
        print("[ERROR] path not found: ", path)
        return False
    # write data to file
    with open(os.path.join(path, filename), method) as file:
        for key, value in data.items():
            file.write(f"{key}:{value},")
        file.write("\n")
    return True


def write_dict_to_json_file(data: dict, path: str, filename: str, method: str = "w") -> bool:
    if not check_for_folder(path):
        print("[ERROR] path not found: ", path)
        return False
    # write data to file
    with open(os.path.join(path, filename), method) as json_file:
        json.dump(data, json_file)
    return True


def read_dict_from_json_file(path: str, filename: str) -> dict:
    json_data: dict = {}
    file_path = os.path.join(path, filename)
    if not check_if_file_exists(file_path):
        print(f"[ERROR] file not found: {filename}")
        return {}
    # read data from file
    with open(file_path, "r") as json_file:
        json_data = json.load(json_file)
    return json_data


def read_list_from_file(path: str, filename: str) -> list:
    dataList: list = []
    file_path = os.path.join(path, filename)
    if check_if_file_exists(file_path):
        print(f"[ERROR] file not found: {filename}")
        return []
    # read data from file
    with open(file_path, "r") as file:
        data: list = file.readlines()
        for line in data:
            dataList.append(line.strip())
    return dataList


# write string to debug file
def debug_log(data: str, mode: str = "a", log_location=os.getcwd()) -> bool:
    if not check_for_folder(log_location):
        print("[ERROR] log path not found: ", log_location)
        return False
    # write data to file
    date = datetime.datetime.now()
    dateFormat = date.strftime("%d-%b-%Y %H:%M:%S")
    filename = "debug_log.txt"
    with open(os.path.join(log_location, filename), mode) as log:
        log.write(f"{dateFormat} >< {data}\n")
    return True


# read list of dictonaries from file
def read_list_of_dict_from_file(path: str, filename: str) -> list:
    dataList: list = []
    file_path = os.path.join(path, filename)
    if check_if_file_exists(file_path):
        print(f"[ERROR] file not found: {filename}")
        return []
    # read data from file
    with open(file_path, "r") as file:
        data: list = file.readlines()
        for line in data:
            dataList.append(ast.literal_eval(line))
    return dataList