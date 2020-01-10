#!/usr/bin/python3
"""
Function that divides elements of a matrix


"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix

    Arguments:

    matrix: must be a list of lists ints or floats
    with rows of the same size

    div: must be a number int or float and not 0


    Result is rounded to 2 decimal places
    and a new matrix is generated

    Raise TypeError or ZeroDivisionError if conditions not
    met

    """

    if not matrix or \
       not isinstance(matrix, list) or \
       not all(isinstance(i, list) for i in matrix) or \
       not all(len(j) for j in matrix) or \
       not all([all(isinstance(k, (int, float)) for k in m) for m in matrix]):

        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)

    checkl = [len(r) for r in matrix]

    if len(set(checkl)) != 1:
        msg = "Each row of the matrix must have the same size"
        raise TypeError(msg)

    if not isinstance(div, (int, float)) or div != div:
        msg = "div must be a number"
        raise TypeError(msg)

    if div == 0:
        msg = "division by zero"
        raise ZeroDivisionError(msg)

    new_m = [[round(j / div, 2) for j in i] for i in matrix]
    return (new_m)
