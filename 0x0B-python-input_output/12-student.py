#!/usr/bin/python3

""" Student to json """


class Student:
    """ Class that defines a Student object """

    def __init__(self, first_name, last_name, age):
        """ Class Constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves Class dictionary base on attr
        If attr is a list of strings, only attributes contained in that list
        will be retrieved

        Otherwise all  attributes will be retrieved
        """
        if not isinstance(attrs, list) or \
           not all(isinstance(i, str) for i in attrs):

            dic = self.__dict__.copy()
        else:

            dic = {i: self.__dict__[i] for i in attrs if i in self.__dict__}

        return dic
