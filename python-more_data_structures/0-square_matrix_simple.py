#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix_a = []
    new_matrix_b = []
    for row in matrix:
        new_matrix_a = list(map(lambda value: value*value, row))
        new_matrix_b.append(new_matrix_a)
    return new_matrix_b
