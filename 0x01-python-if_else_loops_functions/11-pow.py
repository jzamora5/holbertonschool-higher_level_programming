#!/usr/bin/python3
def pow(a, b):
    res = a
    if b == 0:
        return (1)
    elif b < 0:
        res = 1
        for i in range(b * -1):
            res /= a
    else:
        for i in range(b - 1):
            res *= a
    return (res)
