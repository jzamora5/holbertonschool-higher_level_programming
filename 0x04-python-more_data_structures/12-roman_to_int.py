#!/usr/bin/python3
def roman_to_int(roman_string):
    from functools import reduce
    if not roman_string or not isinstance(roman_string, str):
        return (0)
    Roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    dlist = [Roman[i] for i in roman_string]
    dec = reduce(lambda x, y: x + y, dlist)
    return (dec)
