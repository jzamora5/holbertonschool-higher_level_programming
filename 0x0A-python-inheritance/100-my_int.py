#!/usr/bin/python3

""" Class that inherits from int """


class MyInt(int):
    """ Class int rebel == and != are inverted"""

    def __eq__(self, other):
        """ Super Call to Not Equal """
        return super().__ne__(other)

    def __ne__(self, other):
        """ Super Call to Equal """
        return super().__eq__(other)
