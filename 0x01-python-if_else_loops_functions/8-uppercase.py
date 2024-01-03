#!/usr/bin/python3
def uppercase(str):
    for num in range(len(str)):
        if (ord(str[num]) >= 97 and ord(str[num]) <= 122):
            print("{:c}".format(ord(str[num]) - 32) if (num < (len(str) - 1)
            and len(str) != 0)
            else "{:c}\n".format(ord(str[num]) - 32), end="")
        else:
            print(str[num] if (num < (len(str) - 1) and len(str) != 0)
            else "{:c}\n".format(ord(str[num]) - 32), end="")
