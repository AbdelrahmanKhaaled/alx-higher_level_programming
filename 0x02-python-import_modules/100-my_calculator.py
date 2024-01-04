#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    args = sys.argv[1:]
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if args[1] == "+":
        print("{} + {} = {}".format(int(args[0]), int(args[2]), add(int(args[0]), int(args[2]))))
    elif args[1] == "-":
        print("{} - {} = {}".format(int(args[0]), int(args[2]), sub(int(args[0]), int(args[2]))))
    elif args[1] == "*":
        print("{} * {} = {}".format(int(args[0]), int(args[2]), mul(int(args[0]), int(args[2]))))
    elif args[1] == "/":
        print("{} / {} = {}".format(int(args[0]), int(args[2]), div(int(args[0]), int(args[2]))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
