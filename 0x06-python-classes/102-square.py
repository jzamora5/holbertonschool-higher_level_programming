#!/usr/bin/python3
class Square:

    """ Class Square that defines methods and attributes for a square object"""

    def __init__(self, size=0):
        """ Class Constructor """
        self.size = size

    def __eq__(self, other):
        """ Equal """
        return self.area() == other.area()

    def __ne__(self, other):
        """ Not equal """
        return self.area() != other.area()

    def __gt__(self, other):
        """ Greater than """
        return self.area() > other.area()

    def __ge__(self, other):
        """ Greater or Equal """
        return self.area() >= other.area()

    def __le__(self, other):
        """ Less or Equal """
        return self.area() <= other.area()

    def __lt__(self, other):
        """ Less than  """
        return self.area() < other.area()

    @property
    def size(self):
        """ Private Attribute size Getter """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Private Attribute size Setter """
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Method that calculates current square area """
        return (self.__size * self.__size)
