#!/usr/bin/python3
""" save object to file  """

import json


def save_to_json_file(my_obj, filename):
    """ function that returns an object (Python data structure) represented
    by a JSON string"""

    with open(filename, "w") as myfile:
        json.dump(my_obj, myfile)
