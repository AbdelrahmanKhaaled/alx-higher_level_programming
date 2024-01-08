#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for num in list:
            if list.index(num) == len(list) - 1:
                print("{}".format(num))
            else:
                 print("{}".format(num), end=" ")
