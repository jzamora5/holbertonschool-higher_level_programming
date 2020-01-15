#!/usr/bin/python3
class Rectangle:
    """ Class that creates an object Rectangle """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Constructor """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ Method for area calculation """
        return self.width * self.height

    def perimeter(self):
        """ Method for perimeter calculation """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.width + self.height))

    def __str__(self):
        """ Returns the Rectangle for printing """
        recstr = ""
        if self.width == 0 or self.height == 0:
            return (recstr)
        else:
            sym = str(self.print_symbol)
            for j in range(self.height):
                recstr += "{}".format(sym * self.__width)
                if j != (self.height - 1):
                    recstr += "\n"
        return recstr

    def __repr__(self):
        """ Method that returns Object Representation as string """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Action when object is deleted """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Static Method for checking area equality """
        if not isinstance(rect_1, Rectangle):
            msg = "rect_1 must be an instance of Rectangle"
            raise TypeError(msg)
        if not isinstance(rect_2, Rectangle):
            msg = "rect_2 must be an instance of Rectangle"
            raise TypeError(msg)

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            rect_2
