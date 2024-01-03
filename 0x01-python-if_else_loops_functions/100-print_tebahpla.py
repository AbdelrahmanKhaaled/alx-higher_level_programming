#!/usr/bin/python3
for num in range(122, 97, -1):
    print("{:c}".format(num) if num % 2 == 0 else "{:c}".format(num - 32))
