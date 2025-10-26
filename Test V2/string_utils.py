import string_utils

def halve_strings(string_list):
    string_tuple_list = []
    for string in string_list:
        string_tuple_list.append(string_utils.halve_string(string))
    
    return string_tuple_list