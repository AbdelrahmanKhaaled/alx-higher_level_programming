#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1

    args = sys.argv
    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if args[2] == "+":
            print("{} + {} = {}".format(args[1], args[3], add(args[1], args[3])))
        elif args[2] == "-":
            print("{} - {} = {}".format(args[1], args[3], sub(args[1], args[3])))
        elif args[2] == "*":
            print("{} * {} = {}".format(args[1], args[3], mul(args[1], args[3])))
        elif args[2] == "/":
            print("{} / {} = {}".format(args[1], args[3], div(args[1], args[3])))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
