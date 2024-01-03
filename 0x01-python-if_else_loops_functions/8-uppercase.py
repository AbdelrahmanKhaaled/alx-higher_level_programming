#!/usr/bin/python3
def uppercase(str):
    for n in range(len(str)):
        if (n == len(str) - 1):
            f = True
            ss = "{:c}\n".format(ord(str[n]) - 32)
        if (ord(str[n]) >= 97 and ord(str[n]) <= 122):
            print("{:c}".format(ord(str[n])) - 32 if f else ss, end="")
        else:
            print((str[n]) if f else ss, end="")
