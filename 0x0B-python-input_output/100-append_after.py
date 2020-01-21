#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    """ function that inserts a line of text to a file, after each line
    containing a specific string"""

    with open(filename, "r+") as myfile:
        lines = myfile.readlines()
        newline = []
        for i in range(len(lines)):
            newline.append(lines[i])
            if search_string in lines[i]:
                newline.append(new_string)

        myfile.seek(0)
        myfile.write("".join(newline))
