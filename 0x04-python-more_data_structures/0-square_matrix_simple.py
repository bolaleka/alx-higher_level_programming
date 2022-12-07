#!/usr/bin/pytho3

def square_matrix_simple(matrix=[]):
    res = list(map(lambda i: list(map(lambda j: j * j, i)), matrix))
    return res
