#!/usr/bin/python3
def remove_char_at(str, n):
    count = 0
    for num in range(len(str)):
        if (num != n):
            name[count] = str[num]
            count = count + 1
        else:
