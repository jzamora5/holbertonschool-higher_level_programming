#!/usr/bin/python3

""" Module of Base Class for Geometry Rectangle and Square """

import json
import csv
import turtle


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

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draws Rectangles and Squares in GUI """

        if (not list_rectangles and not list_squares) or \
           (len(list_rectangles) == 0 and len(list_squares) == 0):
            return

        def drawfig(x, y, widthfig, heightfig, xoffset, yoffset, color,
                    dd,  gr=turtle.Turtle()):
            # Dot Distance
            dd = dd
            # Dot Size
            dz = 2
            # Angle 90 so it goes to next row
            mov = 90

            gr.goto(xoffset, yoffset)

            # Y Movement

            width = 1
            height = y
            for i in range(height):
                for j in range(width):
                    gr.dot(dz, "black")
                    gr.forward(dd)
                gr.backward(dd * width)
                gr.right(mov)
                gr.forward(dd)
                gr.left(mov)

            gr.goto(xoffset, -1 * y * dd + yoffset)

            # X Movement

            width = x
            height = 1
            for i in range(height):
                for j in range(width):
                    gr.dot(dz, "black")
                    gr.forward(dd)
                gr.backward(dd * width)
                gr.right(mov)
                gr.forward(dd)
                gr.left(mov)

            gr.goto(x * dd + xoffset, -1 * y * dd + yoffset)

            # Draw Figure

            width = widthfig
            height = heightfig
            for y in range(height):
                for i in range(width):
                    gr.dot(dz, color)
                    gr.forward(dd)
                gr.backward(dd * width)
                gr.right(mov)
                gr.forward(dd)
                gr.left(mov)

        # MAIN =========================================================
        gr = turtle.Turtle()

        # Dont show pen when drawing
        gr.penup()
        gr.pen(shown=False)

        # Animation Speed
        # gr.speed(0)

        # Disable Animation
        # turtle.setup(2000, 2000)
        turtle.tracer(False)

        colors = ["blue", "green", "red", "purple",
                  "brown", "orange", "gold"]
        cl = 0
        # Distance between dots
        dd = 3
        # Space between figs
        space = 10
        # Offset movement
        xoffset = -950
        yoffset = 450
        width, height, x, y = 0, 0, 0, 0
        for r in list_rectangles:
            xoffset += (x + width) * dd + space
            width, height = r.width, r.height
            x, y = r.x, r.y
            drawfig(x, y, width, height, xoffset, yoffset, colors[cl], dd, gr)
            cl = cl + 1 if cl < 5 else 0

        yoffset = 0
        ct = 0
        for s in list_squares:
            if ct == 0:
                xoffset = (dd + space) - 950
                ct = 1
            else:
                xoffset += (x + width) * dd + space
            width, height = s.size, s.size
            x, y = s.x, s.y
            drawfig(x, y, width, height, xoffset, yoffset, colors[cl], dd, gr)
            cl = cl + 1 if cl < 5 else 0

        turtle.done()
