#!/usr/bin/python3
def remove_char_at(str, n):
    for num in range(len(str)):
        if (num == n):
            str = str[0:num] + str[num + 1:]
            return str
    return str
