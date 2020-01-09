#!/usr/bin/python3
class Square:

    """ Class Square that defines methods and attributes for a square object"""

    def __init__(self, size=0):
        """ Class Constructor"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
