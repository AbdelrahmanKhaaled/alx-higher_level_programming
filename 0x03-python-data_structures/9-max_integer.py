#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    list2 = []
    for num in my_list:
        list2.append(num)
    list2.sort()
    return list2[-1]
        
