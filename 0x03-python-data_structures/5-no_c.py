#!/usr/bin/python3
def no_c(my_string):
    end = 0
    str2 = ""
    for c in my_string:
        if c == "c" or c == "C":
            str2 += my_string[:end]
            my_string = my_string[end + 1:]
            end = -1
        end += 1
    str2 += my_string
    return str2
