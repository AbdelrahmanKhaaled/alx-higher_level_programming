#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    if len(arguments) == 0:
        print("0 arguments.")
    elif len(arguments) == 1:
        print("{} argument:".format(len(arguments)))
        for num in range(len(arguments)):
            print("{}: {}".format(num + 1, arguments[num]))
    else:
        print("{} arguments:".format(len(arguments)))
        for num in range(len(arguments)):
            print("{}: {}".format(num + 1, arguments[num]))
