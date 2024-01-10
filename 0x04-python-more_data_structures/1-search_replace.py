#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for num in my_list:
        if num == 2:
            new_list.append(89)
        else:
            new_list.append(num)
    return new_list
