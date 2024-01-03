#!/usr/bin/python3
def remove_char_at(str, n):
    flag = False
    for num in range(len(str)):
        if (num == n or num > n):
            str[num] = str[num + 1]
            flag = True
    if flag:
        str = str[0:-1]
    return str
