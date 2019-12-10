#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        s1 = str[:n]
        s2 = str[n + 1:]
        return (s1 + s2)
    else:
        return (str)
