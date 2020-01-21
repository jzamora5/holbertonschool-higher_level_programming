#!/usr/bin/python3

""" script that reads stdin line by line and computes metrics """

import sys


def printsts(dic, size):
    """ Prints information """
    print("File size: {:d}".format(size))
    for i in sorted(dic.keys()):
        if dic[i] != 0:
            print("{:s}: {:d}".format(i, dic[i]))


sts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
       "404": 0, "405": 0, "500": 0}

count = 0
size = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            printsts(sts, size)

        stlist = line.split()

        if stlist[-2] in sts:
            sts[stlist[-2]] += 1

        size += int(stlist[-1])
        count += 1

except KeyboardInterrupt:
    printsts(sts, size)
    raise
