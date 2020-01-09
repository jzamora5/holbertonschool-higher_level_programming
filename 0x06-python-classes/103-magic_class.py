#!/usr/bin/python3
import math


class MagicClass:
    """ Magic Class for a circle object"""

    def __init__(self, radius=0):
        """ Constructor of Class """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ Area calculation """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """ Circumference Calculation """
        return (2 * math.pi * self.__radius)
