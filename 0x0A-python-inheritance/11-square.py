#!/usr/bin/python3

""" Class that inherits from Rectangle """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class that defines a Square by inheritance of Rectangle class """

    def __init__(self, size):
        """ Constructor """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Area method through Super call """
        return super().area()

    def __str__(self):
        """ Method for when print is used """
        msg = "[Square] {:d}/{:d}".format(self.__size, self.__size)
        return msg
