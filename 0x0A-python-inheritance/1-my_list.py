#!/usr/bin/python3
"""  Class that inherits from list """


class MyList(list):
    """ Class that inherits from list """

    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """
        print(sorted(self))
