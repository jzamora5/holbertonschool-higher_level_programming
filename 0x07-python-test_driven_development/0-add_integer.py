#!/usr/bin/python3
"""
Project for studying doctests in python


"""
def add_integer(a, b=98):
    """Function that adds 2 integers
    If not integers or floats, raise errors
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return int(a + b)
