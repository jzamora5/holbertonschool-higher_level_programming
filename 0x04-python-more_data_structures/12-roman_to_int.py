#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return (0)
    Rm = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    rm = roman_string
    dlist = [Rm[i[0]] if Rm[i[0]] >= Rm[i[1]] else (-1*Rm[i[0]])
             for i in zip(rm, rm[1:] + rm[-1])]
    dec = sum(dlist)
    return (dec)
