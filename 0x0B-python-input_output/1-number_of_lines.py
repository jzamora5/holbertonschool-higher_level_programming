#!/usr/bin/python3


def number_of_lines(filename=""):
    """ function that reads a text file (UTF8) and prints it to stdout """

    with open("my_file_0.txt") as myfile:
        lines = myfile.readlines()
    return len(lines)
