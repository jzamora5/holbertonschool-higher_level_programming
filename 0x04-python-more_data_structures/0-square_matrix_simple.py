#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_m = [[j ** 2 for j in i] for i in matrix]
    return (new_m)
