#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    Max = 0
    target_key = None
    for key, value in a_dictionary.items():
        if Max < value:
            target_key = key
            Max = value
    return target_key
