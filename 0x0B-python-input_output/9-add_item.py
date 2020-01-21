#!/usr/bin/python3

"""
script that adds all arguments to a Python list,
and then save them to a file
"""

from sys import argv
from os import path

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

if path.isfile(filename):
    nlist = load_from_json_file(filename)
else:
    nlist = []

for i in range(1, len(argv)):
    nlist.append(argv[i])

save_to_json_file(nlist, filename)
