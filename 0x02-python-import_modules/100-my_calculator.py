#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    args = sys.argv[1:]
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if args[1] == "+":
            print("{} + {} = {}".format(args[0], args[2], add(args[0], args[2])))
            exit(0)
        elif args[1] == "-":
            print("{} - {} = {}".format(args[0], args[2], sub(args[0], args[2])))
            exit(0)
        elif args[1] == "*":
            print("{} * {} = {}".format(args[0], args[2], mul(args[0], args[2])))
            exit(0)
        elif args[1] == "/":
            print("{} / {} = {}".format(args[0], args[2], div(args[0], args[2])))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
