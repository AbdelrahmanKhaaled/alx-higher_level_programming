#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    b_dict = sorted(a_dictionary.keys())
    for d in b_dict:
        print("{}: {}".format(d, a_dictionary[d]))
