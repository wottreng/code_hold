"""
Purpose:
    * functions for manipulating data
I/O: function specific
Testing: see main function at bottom of file
Revision: 1.0
Language: Python 3.8
Author: Mark Wottreng
"""


# function to reverse order of list
def reverse_list(list_to_reverse: list) -> list:
    return list_to_reverse[::-1]


# function to flip sign of all elements in list
def flip_sign_list(list_to_flip: list) -> list:
    return [-x for x in list_to_flip]


# function to convert list of strings to list of floats
def convert_list_of_strings_to_list_of_floats(list_to_convert: list) -> list:
    return [float(x) for x in list_to_convert]

# function to convert nested lists of strings to nested lists of floats
def convert_nested_list_of_strings_to_nested_list_of_floats(list_to_convert: list) -> list:
    return [[float(x) for x in y] for y in list_to_convert]


# function to convert list of strings to list of ints
def convert_list_of_strings_to_list_of_ints(list_to_convert: list) -> list:
    return [int(x) for x in list_to_convert]


# function to convert nested lists of strings to nested lists of ints
def convert_nested_list_of_strings_to_nested_list_of_ints(list_to_convert: list) -> list:
    return [[int(x) for x in y] for y in list_to_convert]


if __name__ == "__main__":
    print("[TEST] testing functions")
    test_list = [1, 2, 3, 4, 5, 6, -7, -8, 9, 10]
    reversed_list = reverse_list(test_list)
    print(f"[TEST] reversed list: {reversed_list}")
    sign_flipped_list = flip_sign_list(test_list)
    print(f"[TEST] sign flipped list: {sign_flipped_list}")
    # ----------
    test_list = ["1", "2", "3", "4", "5", "6", "-7", "-8.65", "9.7", "10.2"]
    converted_list = convert_list_of_strings_to_list_of_floats(test_list)
    print(f"[TEST] converted list of floats: {converted_list}")
    # ----------
    test_list = [["1", "2", "3"], ["4.8", "5.2", "6.4"], ["-7", "-8", "9"], ["10"]]
    converted_list = convert_nested_list_of_strings_to_nested_list_of_floats(test_list)
    print(f"[TEST] converted list of floats: {converted_list}")
    # ----------
    test_list = ["1", "2", "3", "4", "5", "6", "-7", "-8", "9", "10"]
    converted_list = convert_list_of_strings_to_list_of_ints(test_list)
    print(f"[TEST] converted list of ints: {converted_list}")
    # ----------
    test_list = [["1", "2", "3"], ["4", "5", "6"], ["-7", "-8", "9"], ["10"]]
    converted_list = convert_nested_list_of_strings_to_nested_list_of_ints(test_list)
    print(f"[TEST] converted list of ints: {converted_list}")
    # ----------
