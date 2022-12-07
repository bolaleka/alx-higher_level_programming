#!/usr/bin/pytho3

def square_matrix_simple(matrix=[]):
    res = [[x ** 2 for x in row] for row in matrix]
    return res
