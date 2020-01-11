#!/usr/bin/python3
"""
Function that prints My name is <first name> <last name>


"""


def say_my_name(first_name, last_name=""):
    """
    Prints a Name

    Arguments:

    first_name: must be a string

    last_name: must be a string, if no argument given, then empty by default

    Otherwise a TypeError is raised

    """
    if not isinstance(first_name, str):
        msg = "first_name must be a string"
        raise TypeError(msg)

    if not isinstance(last_name, str):
        msg = "last_name must be a string"
        raise TypeError(msg)

    print("My name is {} {}".format(first_name, last_name))
