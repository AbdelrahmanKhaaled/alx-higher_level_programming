#!/usr/bin/python3
for num in range(100):
    if (num < 10):
        print(f"0{num}, ")
    else:
        print("{}".format(f"{num}, " if num >= 99 else "99"))
        
