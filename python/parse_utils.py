"""
Purpose:
    * functions for aggressively parsing of input data
    * parsing log files where there is no standard formatting
I/O: function specific
Testing: see main function at bottom of file
Revision: 1.3
Language: Python 3.8
Author: Mark Wottreng
"""

import re
import ast

import sys
from pathlib import Path
FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
# ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

from system_utils import * # see system utils: https://github.com/wottreng/code_hold/blob/main/python/system_utils.py


def find_line_that_matches_substring(input_list: list, variable_name: str) -> (int, str):
    """
    * Purpose: find first line that matches a substring and return the line number and line
    :param input_list: list of strings
    :param substring: string, variable name to be found in a larger string
    :return: tuple, line number of input_list where substring is found and entire string that substring is found in
    """
    for line_number in range(len(input_list)):
        if find_substring(input_list[line_number], variable_name)[0] is True:
            return line_number, input_list[line_number]
    return -1, ""
    # --- end of function --- #


def find_first_line_that_has_a_timestamp(input_list: list) -> (int, str):
    """
    * Purpose: find first line with timestamp and return the line number and timestamp
    :param input_list: list of strings
    :return: tuple, line number of input_list where timestamp is found and timestamp string
    """
    for line_number in range(len(input_list)):
        if parse_string_for_timestamp(input_list[line_number]) != "":
            return line_number, parse_string_for_timestamp(input_list[line_number])
    return -1, ""
    # --- end of function --- #


def parse_string_for_timestamp(input_string: str) -> str:
    """
    * Purpose: parse string for timestamp
    :param input_string: any string
    :return: timestamp string
    """
    # find timestamp using regex
    pattern_1 = r"\d{2}:\d{2}:\d{2}\.\d{3}"
    pattern_2 = r"\d{2}:\d{2}:\d{2}"
    timestamp_regex = re.compile(pattern_1 + "|" + pattern_2)
    timestamp_match = timestamp_regex.search(input_string)
    if timestamp_match is not None:
        time_string = timestamp_match.group(0)
        return time_string
    else:
        # print("[ERROR] timestamp not found in string")
        return ""
    # --- end of function --- #


def find_lines_that_match_substring(input_list: list, substring: str) -> list:
    """
    * Purpose: iterate over list of strings and find lines that match a substring
    :param input_list: list of strings
    :param substring: string, variable name to be found in a larger string
    :return: list of strings where substring was found
    """
    return_list: list = []
    for line in input_list:
        if find_substring(line, substring)[0] is True:
            return_list.append(line)
    return return_list
    # --- end of function --- #


def parse_string_list_for_variable_values(input_list: list, variable_names: list) -> list:
    """
    * Purpose: iterate over list of strings and return variable values
    * method: parse a single string for multiple variable names and return their values
    :param input_list: list of strings
    :param variable_names: list of string variable names
    :return: list of dictionaries, keys are variable names and values are parsed values from string
    """
    return_list: list = []
    for line in input_list:
        variable_dict: dict = {}
        for variable_name in variable_names:
            variable_value = parse_string_for_values(line, variable_name)
            if variable_found: variable_dict[variable_name] = variable_value[0]
        return_list.append(variable_dict)
    return return_list
    # --- end of function --- #


def find_substring(input_string: str, substring: str) -> (bool, str):
    """
    * Purpose: find substring in string using different strategies
    * Method: if exact match is not found, make everything lowercase and try to match. if match is found, go back to original string and extract exact substring
    :param input_string: string data
    :param substring: string of data to be found
    :return: tuple, variable found boolean and exact string found
    """
    # stage 1: check if substring is in string
    if input_string.find(substring) != -1:
        return True, substring
    # stage 2: try to find lowercase substring
    input_string_lower = input_string.lower()
    substring_lower = substring.lower()
    input_string_location = input_string_lower.find(substring_lower)
    if input_string_location != -1:
        substring_actual = input_string[input_string_location:input_string_location + len(substring)]
        return True, substring_actual
    # substring not found
    return False, ""
    # --- end of function --- #


def parse_string_for_values(input_string: str, variable_name: str,
                            number_of_returned_values: int = 1,
                            negative_values_possible: bool = True) -> list:
    """
    * Purpose: parse string for variable values
    :param input_string: any string
    :param variable_name: string, variable name to be found
    :param number_of_returned_values: int, number of values to be returned
    :param negative_values_possible: boolean, are negative values possible?
    :return: list of values found. if not found, [None] will be returned
    """
    return_values: list = []
    # find variable name in string
    variable_found, actual_variable_name = find_substring(input_string, variable_name)
    if variable_found is False:
        return [None]
    #
    split_string: list = input_string.split(actual_variable_name)
    #
    if number_of_returned_values == 1:
        substring = ""
        if len(split_string[1]) > 15:
            substring = split_string[1][0:15]
        else:
            substring = split_string[1][0:len(split_string[1])]
        scrubbed_substring: str = remove_non_numeric_characters(substring, negative_values_possible)
        if "." in scrubbed_substring:
            return_values.append(float(scrubbed_substring))
        else:
            return_values.append(int(scrubbed_substring))
        return return_values
    #
    else:  # number_of_returned_values > 1
        if len(split_string[1]) > 15:
            substring = split_string[1][0:30]
        else:
            substring = split_string[1][0:len(split_string[1])]
        split_scrubbed_substring: list = substring.split(",")  # ASSUMPTION: variable values are separated by commas
        for substring in split_scrubbed_substring:
            scrubbed_substring: str = remove_non_numeric_characters(substring, negative_values_possible)
            if "." in scrubbed_substring:
                return_values.append(float(scrubbed_substring))
            else:
                return_values.append(int(scrubbed_substring))
        return return_values
    # --- end of function --- #


def parse_string_for_nonnumerical_value(input_string: str, variable_name: str, possible_values:list) -> str:
    """
    * Purpose: parse string for non-numerical variable values
    :param input_string: any string
    :param variable_name: string, variable name to be found
    :return: string, value of variable, if not found, an empty string will be returned
    """
    # find variable name in string
    input_string_lower = input_string.lower()
    variable_found, actual_variable_name = find_substring(input_string_lower, variable_name)
    if variable_found is False:
        return ""
    #
    split_string: list = input_string_lower.split(actual_variable_name)
    #
    substring = ""
    if len(split_string[1]) > 15:
        substring = split_string[1][0:15]
    else:
        substring = split_string[1][0:len(split_string[1])]
    for possible_value in possible_values:
        if find_substring(substring, possible_value)[0] is True:
            return possible_value
    return ""
    # --- end of function --- #

def find_lines_that_match_substring_list(input_list: list, substring_list: list) -> dict:
    """
    * Purpose: find all lines that match a list of substrings
    :param input_list: list of strings
    :param substring_list: list of variable names to be found
    :return: dictionary of lists for each variable name in substring_list
    """
    return_dict: dict = {}
    for substring in substring_list:
        return_dict[substring] = find_lines_that_match_substring(input_list, substring)
    return return_dict
    # --- end of function --- #


def find_lines_that_match_an_iterable_variable_name(input_list: list, variable_name: str) -> dict:
    """
    * Purpose: find all lines that match a variable name that changes value and format ex. "stage-1", "Stage-2", "stage:3"
    :param input_list: list of strings
    :param variable_name: string, name of variable to be found
    :return: dictionary of lists. keys are found in input_list which match variable_name
    """
    return_dict: dict = {}
    # find all lines that match variable name
    filtered_list: list = find_lines_that_match_substring(input_list, variable_name)
    # parse lines for variable name value and build combined variable name list
    list_of_all_different_variable_values: list = []
    for line in filtered_list:
        _, actual_variable_name = find_substring(line, variable_name)
        variable_name_value: list = parse_string_for_values(line, actual_variable_name, 1, False)
        if variable_name_value[0] is None: continue
        variable_name_combined = (actual_variable_name + "-" + str(variable_name_value[0])).lower()
        if variable_name_combined not in list_of_all_different_variable_values:
            list_of_all_different_variable_values.append(variable_name_combined)
            return_dict[variable_name_combined] = []  # initiate list
        return_dict[variable_name_combined].append(line)
    #
    if len(return_dict.keys()) == 0: non_fatal_error(f"-> no {variable_name} data found")
    return return_dict
    # --- end of function --- #


def build_list_for_variable(input_list: list, variable_name: str) -> list:
    """
    * Purpose: build list for variable from list of dictionaries
    :param input_list: list of dictionaries
    :param variable_name: string, name of variable to be found
    :return: list of variable values
    """
    return_list: list = []
    for variable_dict in input_list:
        if "{" in variable_dict and "}" in variable_dict:
            variable_dict = ast.literal_eval(variable_dict)
        return_list.append(variable_dict[variable_name])
    return return_list
    # --- end of function --- #


# ========= SUPPORT FUNCTIONS =========

def remove_non_numeric_characters(input_string: str, negative_values_possible: bool = True) -> str:
    """
    * Purpose: remove all characters that are not numbers and return string value
    :param input_string: any string
    :param negative_values_possible: boolean, care negative values possible in return value?
    :return: string of parsed value
    """
    return_string: str = ""
    numbers_found_flag: bool = False
    acceptable_values: list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
    if negative_values_possible is True:
        acceptable_values.append("-")
    for character in input_string:
        if character in acceptable_values:
            return_string += character
            numbers_found_flag = True
        elif numbers_found_flag is True and character.isdigit() is False:
            break
    return return_string
    # --- end of function --- #


# ========= TEST FUNCTION =========

if __name__ == "__main__":
    test_list = [
        "00:01:10 some_function_name.234324   main  0 4 211.22.0-0 D: [stuff] Stage-1: long = 9.56, lat = 1.35, xy {-1.2, 10.3} tracking loc: 145",
        "Jan 01 00:01:14 some_function_name.234324  blahblah main  0 4 211.22.0-0 D: [stuff] stage-2 : Long = -4.3, lat = 5.4, xy = {3.24,-1.2} tracking loc: 234",
        "Jan 01 00:01:14.713 some_function_name.234324   main  0 4 211.22.0-0 D: [stuff] Trailer found: yes {} long = 5.234, lat = 6.012, xy {-1.2, 10.3} tracking loc: 145",
        "00:01:16.45 some_function_name.234324   main  0 4 211.22.0-0 D: [stuff] Stage-3: long= 0.2, lat = 0.56, xy {0.3, 0.3} tracking loc: 23"
    ]

    print("[TEST] parse_string_for_values")
    test_string = test_list[1]
    variable_found, var_name = find_substring(test_string, "long")  # True, "long"
    print("[PASSED]") if variable_found is True else print("[FAILED]")
    # if variable_found is True:
    #     print(parse_string_for_values(test_string, var_name))  # [-4.3]
    print("-----------------------------------------------------")
    print("[TEST] parse list for values")
    return_list = parse_string_list_for_variable_values(test_list, ["long", "lat"])
    # print(return_list)  #  [{'long': 9.56, 'lat': 1.35}, {'long': -4.3, 'lat': 5.4}, {'long': 5.234, 'lat': 6.012}, {'long': 0.2, 'lat': 0.56}]
    # print("long value in list: ", return_list[0]["long"])  # 9.56
    print("[PASSED]") if return_list[0]["long"] == 9.56 else print("[FAILED]")
    print("-----------------------------------------------------")
    print("[TEST] parse string for timestamp")
    test_string = test_list[2]
    timestamp = parse_string_for_timestamp(test_string)
    # print("timestamp: " + timestamp)  # "00:01:14.713"
    print("[PASSED]") if timestamp == "00:01:14.713" else print("[FAILED]")
    print("-----------------------------------------------------")
    print("[TEST] parse string for multiple values")
    test_string = test_list[0]
    # print(parse_string_for_values(test_string, "xy", number_of_returned_values=2))  # [-1.2, 10.3]
    print("[PASSED]") if parse_string_for_values(test_string, "xy", number_of_returned_values=2) == [-1.2, 10.3] else print("[FAILED]")
    print("-----------------------------------------------------")
    print("[TEST] find line with first timestamp")
    line_number, timestamp = find_first_line_that_has_a_timestamp(test_list)
    # print(f"line number: {line_number}, timestamp: {timestamp}")
    print("[PASSED]") if line_number == 0 and timestamp == "00:01:10" else print("[FAILED]")
    print("-----------------------------------------------------")
    print("[TEST] find first line that matches a substring")
    line_number, line = find_line_that_matches_substring(test_list, "blahblah")
    # print("line number: ", line_number)  # 1
    print("[PASSED]") if line_number == 1 else print("[FAILED]")
    print("-----------------------------------------------------")
    print("[TEST] find all lines that match a list of substring")
    substring_dict: dict = find_lines_that_match_substring_list(test_list, ["Stage-1", "stage-2", "Stage3"])
    # print(substring_dict)  # {'Stage-1': [1], 'stage-2': [1], 'Stage3': [0]}
    # print(substring_dict["Stage-1"])  # ["<line content>"]
    print("[PASSED]") if substring_dict["Stage-1"] == ["00:01:10 some_function_name.234324   main  0 4 211.22.0-0 D: [stuff] Stage-1: long = 9.56, lat = 1.35, xy {-1.2, 10.3} tracking loc: 145"] else print("[FAILED]")
    print("-----------------------------------------------------")
    print("[TEST] find all lines that match a iterable variable name")
    variable_name_dict: dict = find_lines_that_match_an_iterable_variable_name(test_list, "stage")
    # print(variable_name_dict)  # {'stage-1': [1], 'stage-2': [1], 'stage-3': [1]}
    print("[PASSED]") if variable_name_dict["stage-1"] == ["00:01:10 some_function_name.234324   main  0 4 211.22.0-0 D: [stuff] Stage-1: long = 9.56, lat = 1.35, xy {-1.2, 10.3} tracking loc: 145"] else print("[FAILED]")
    print("-----------------------------------------------------")
    print("[TEST] build list for variable from list of dictionaries")
    variable_list = build_list_for_variable(return_list, "long")
    # print(variable_list)  # [9.56, -4.3, 5.234, 0.2]
    print("[PASSED]") if variable_list == [9.56, -4.3, 5.234, 0.2] else print("[FAILED]")
    print("-----------------------------------------------------")
    print("[TEST] find non-numeric variable value")
    test_string = test_list[2]
    variable_value = parse_string_for_nonnumerical_value(test_string, "Trailer found", ["yes", "no"])
    # print(variable_value)  # "yes"
    print("[PASSED]") if variable_value == "yes" else print("[FAILED]")
    # --- end of test --- #
