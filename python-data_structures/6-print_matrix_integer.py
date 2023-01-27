#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for n in range(0, len(i)):
            if n - 1 < len(i):
                print("{}".format(i[n]), end="")
            if n - 2 < len(i):
                print(" ", end="")
        print()
