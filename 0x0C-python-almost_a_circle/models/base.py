#!/usr/bin/python3

""" Module of Base Class for Geometry Rectangle and Square """

import json
import csv


class Base:
    """ Class to define base model Object """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

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

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if not json_string or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances from a file """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, encoding="utf-8") as myfile:
                rd = myfile.read()
                dicst = cls.from_json_string(rd)
                inslist = []
                for i in dicst:
                    inslist.append(cls.create(**i))
                return inslist
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes to CSV and saves to file """
        filename = cls.__name__ + ".csv"
        csvlist = []
        if list_objs:
            for i in list_objs:
                dic = i.to_dictionary()
                if cls.__name__ == "Rectangle":
                    csvlist.append([dic["id"], dic["width"],
                                    dic["height"], dic["x"], dic["y"]])

                elif cls.__name__ == "Square":
                    csvlist.append([dic["id"], dic["size"],
                                    dic["x"], dic["y"]])

        with open(filename, "w", encoding="utf-8") as myfile:
            w = csv.writer(myfile)
            w.writerows(csvlist)

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes from CSV and loads from file """
        filename = cls.__name__ + ".csv"

        try:
            with open(filename, encoding="utf-8") as myfile:
                r = csv.reader(myfile)
                if cls.__name__ == "Rectangle":
                    attr = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    attr = ["id", "size", "x", "y"]
                inslist = []
                for row in r:
                    ct, dic = 0, {}
                    for i in row:
                        dic[attr[ct]] = int(i)
                        ct += 1
                    inslist.append(cls.create(**dic))
                return inslist
        except IOError:
            return []
