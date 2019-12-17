#!/usr/bin/python3
def no_c(my_string):
    slist = list(my_string)
    [slist.remove(i) for i in slist if i == 'c' or i == 'C']
    return("".join(slist))
