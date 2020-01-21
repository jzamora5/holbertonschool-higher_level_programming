#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    """ function that inserts a line of text to a file, after each line
    containing a specific string"""

    with open(filename, "r+") as myfile:
        lines = myfile.readlines()

        for i in range(len(lines)):
            if search_string in lines[i]:
                lines.insert(i + 1, new_string)

        myfile.seek(0)
        myfile.write("".join(lines))
