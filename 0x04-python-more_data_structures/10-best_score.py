#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    else:
        Max = Max = list(a_dictionary.values())[0]
        for value in list(a_dictionary.values()):
            if Max < value:
                Max = value
        return Max

