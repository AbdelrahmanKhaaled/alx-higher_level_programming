#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key_i, value_i in list(a_dictionary.items()):
        if value_i == value:
            del a_dictionary[key_i]
    return a_dictionary
