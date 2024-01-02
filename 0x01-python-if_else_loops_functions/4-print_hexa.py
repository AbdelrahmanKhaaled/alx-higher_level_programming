#!/usr/bin/python3
for num in range(99):
    if (num % 16 <= 9 and num / 16 > 0):
        print(f"0x{num}")
    elif (num % 16 > 9 and num % 16 < 16 and num / 16 > 0):
        print(f"0x{:c}".format(num + 87))
    if (num % 16 <= 9):
        print(f"0x{num / 16}{num % 16}")
    elif (num % 16 > 9 and num % 16 < 16):
        print("0x{:d}{:c}".format(num / 16, (num % 16) + 87)))
