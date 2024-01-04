#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sums = 0
    for num in sys.argv[1:]:
        sums = sums + int(num)
    print(sums)
