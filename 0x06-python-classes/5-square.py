#!/usr/bin/python3
class Square:

    """ Class Square that defines methods and attributes for a square object"""

    def __init__(self, size=0):
        """ Class Constructor"""
        self.size = size

    @property
    def size(self):
        """ Private Attribute size Getter """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Private Attribute size Setter """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Method that calculates current square area """
        return (self.__size * self.__size)

    def my_print(self):
        """ Method that prints in stdout the square with the char # """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print('#' * self.size)
