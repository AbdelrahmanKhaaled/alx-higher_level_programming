#!/usr/bin/python3
for num in range(100):
    if (num < 10):
        print(f"0{num}, ", end="")
    else:
        print("{}".format(f"{num}, " if num <= 99 else "99\n"), end="")
