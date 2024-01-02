#!/usr/bin/python3
def uppercase(str):
    for num in range(len(str)):
        if (ord(str[num]) >= 97 and ord(str[num]) <= 122):
            print("{:c}".format(ord(str[num]) - 32))
        else:
             print(str[num])
