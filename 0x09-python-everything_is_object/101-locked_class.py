#!/usr/bin/python3
class LockedClass:
    """ Class without __dict__ and locked attributes """
    __slots__ = "first_name"
