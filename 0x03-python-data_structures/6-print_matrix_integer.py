#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matix:
        return None
    for list in matrix:
        if len(list) == 0:
            print()
        for num in list:
            if list.index(num) == len(list) - 1:
                print("{:d}".format(num))
            else:
                print("{:d}".format(num), end=" ")
