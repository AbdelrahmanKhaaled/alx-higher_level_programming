#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None or len(a_dictionary) == 0:
        return None
    else:
        Max = list(a_dictionary.values())[0]
        target_key = list(a_dictionary.keys())[0]
        for key, value in list(a_dictionary.items()):
            if Max < value:
                target_key = key
                Max = value
        return target_key
