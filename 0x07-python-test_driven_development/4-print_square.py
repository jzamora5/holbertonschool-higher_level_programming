#!/usr/bin/python3
"""
Function that prints a square with the character '#'


"""


def print_square(size):
    """
    Prints a square using the '#' character

    Arguments:

    size: is the size length of the square

    it must be a interger otherwise a TypeError will be raised

    is size is less than 0, a ValueError will be raise

    """

    if not isinstance(size, int):
        msg = "size must be an integer"
        raise TypeError(msg)

    if size < 0:
        msg = "size must be >= 0"
        raise ValueError(msg)

    for i in range(size):
        print('#' * size)
