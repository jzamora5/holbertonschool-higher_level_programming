#!/usr/bin/python3


def read_file(filename=""):
    """ function that reads a text file (UTF8) and prints it to stdout """

    with open("my_file_0.txt", encoding="utf-8") as myfile:
        print(myfile.read(), end='')
