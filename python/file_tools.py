import os
import datetime
import json
'''
module for reading and writing data
Version 1.3
written by Mark Wottreng
'''

def write_string_to_file(data: str, path: str = os.getcwd(), filename: str = "data.txt", method: str = "w"):
    with open(f"{path}/{filename}", method) as file:
        file.write(f"{data}\n")
    #print(f"data writen to: {filename}")
    return True

def write_list_to_file(data: list, path: str = os.getcwd(), filename: str = "dataList.txt", method: str = "w"):
    with open(f"{path}/{filename}", method) as file:
        for line in data:
            file.write(f"{line}\n")
    #print(f"data list written to: {filename}")
    return True

def write_dict_to_file(data: dict, path: str = os.getcwd(), filename: str = "dataList.txt", method: str = "w"):
    with open(f"{path}/{filename}", method) as file:
        for key, value in data.items():
            file.write(f"{key}:{value},")
        file.write("\n")
    #print(f"data dict written to: {filename}")
    return True

def write_dict_to_json_file(data:dict = {}, path: str = os.getcwd(), filename: str = "data.json", method: str = "w"):
    with open(f"{path}/{filename}", method) as json_file:
        json.dump(data, json_file)
    return True

def read_dict_from_json_file(path: str = os.getcwd(), filename: str = "data.json"):
    try:
        with open(f"{path}/{filename}", "r") as json_file:
            json_data = json.load(json_file)
        return json_data
    except:
        print(f"[!] file not found: {filename}")
        return False

def read_list_from_file(path: str = os.getcwd(), filename: str = "dataList.txt"):
    dataList: list = []
    try:
        with open(f"{path}/{filename}", "r") as file:
            data: list = file.readlines()
        for line in data:
            dataList.append(line.strip())
        return dataList
    except:
        print(f"[!] file not found: {filename}")
        return False

def debug_log(data: str, mode: str = "a", log_location=os.getcwd()):
    date = datetime.datetime.now()
    dateFormat = date.strftime("%d-%b-%Y %H:%M:%S")
    with open(f"{log_location}/debug_log.txt", mode) as log:
        log.write(f"{dateFormat} >< {data}\n")
    return True
#
