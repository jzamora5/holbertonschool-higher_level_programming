#!/usr/bin/python3
class Rectangle:
    """Constructor for Class Rectangle """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Width Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width Setter """
        if not isinstance(value, int):
            msg = "width must be an integer"
            raise TypeError(msg)
        if (value < 0):
            msg = "width must be >= 0"
            raise ValueError(msg)
        self.__width = value

    @property
    def height(self):
        """ Height Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height Setter """
        if not isinstance(value, int):
            msg = "height must be an integer"
            raise TypeError(msg)
        if (value < 0):
            msg = "height must be >= 0"
            raise ValueError(msg)
        self.__height = value
