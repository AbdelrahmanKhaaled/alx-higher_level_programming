#!/usr/bin/python3
def fizzbuzz():
    for num in range(1,100):
        if (num % 3 == 0 and num % 5 == 0):
            print("FizzBuuz ", end="")
        elif (num % 3 == 0):
            print("Fizz ", end="")
        elif (num % 5 == 0):
            print("Buzz ", end="")
        else:
            print(f"{num} ", end="")
    print("FizzBuuz", end="")
