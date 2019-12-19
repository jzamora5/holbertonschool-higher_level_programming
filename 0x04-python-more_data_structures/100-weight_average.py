#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    a = sum(i[0] * i[1] for i in my_list)
    n = sum(j[1] for j in my_list)
    return (a / n)
