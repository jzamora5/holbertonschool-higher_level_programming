#!/usr/bin/python3

import json

class Base:
    """ Class to define base model Object """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """  writes the JSON string representation of list_objs to a file """
        jlist = []
        filename = cls.__name__ + ".json"
        if list_objs:
            for i in list_objs:
                jlist.append(i.to_dictionary())

        st = cls.to_json_string(jlist)
        with open(filename, "w", encoding="utf-8") as myfile:
            myfile.write(st)
