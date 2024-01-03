#!/usr/bin/python3
for num in range(9):
    for num2 in range(9):
        if (num == num2 and num > num2):
            continue
        else:
            print("{:d}{:d}, ".format(num, num2), end="")
print(89)
