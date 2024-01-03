#!/usr/bin/python3
def uppercase(str):
    for n in range(len(str)):
        ss = f"{:c}\n".format(ord(str[n]) - 32)
        f = False
        if (n != len(str) - 1):
            f = True
        if (ord(str[n]) >= 97 and ord(str[n]) <= 122):
            print("{:c}".format(ord(str[n])) - 32 if f else ss, end="")
        else:
            print((str[n]) if f else ss, end="")
