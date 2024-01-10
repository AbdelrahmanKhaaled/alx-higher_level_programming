#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        summ = 0
        under = 0
        for tuplee in my_list:
            x, y = tuplee
            summ += x * y
            under += y
        return summ / under
