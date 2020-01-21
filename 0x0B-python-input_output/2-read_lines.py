#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    """ function that reads n lines of a text file (UTF8) and prints it
    to stdout"""

    with open(filename) as myfile:
        lines = myfile.readlines()
        if nb_lines <= 0 or nb_lines >= len(lines):
            [print(i, end='') for i in lines]
        else:
            [print(lines[i], end='') for i in range(0, nb_lines)]
