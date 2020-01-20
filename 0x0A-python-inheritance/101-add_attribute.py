#!/usr/bin/python3


def add_attribute(obj, name, value):
    """ Function to add new attribute IF possible (object has __dict__()) """

    if not hasattr(obj, "__dict__"):
        msg = "can't add new attribute"
        raise TypeError(msg)
    setattr(obj, name, value)
