#!/usr/bin/python3
for num in range(9):
    for num2 in range(10):
        if (num == num2 or num > num2):
            continue
        elif (num < 8):
            print("{:d}{:d}, ".format(num, num2), end="")
print(89)
