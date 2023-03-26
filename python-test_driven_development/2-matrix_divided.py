#!/usr/bin/python3
""" task 1 """


def matrix_divided(matrix, div):
    for idx, row in enumerate(matrix):
        if idx < len(matrix) - 1 and len(matrix[idx]) != len(matrix[idx + 1]):
            raise TypeError(f"Each row of the matrix"
                            f" must have the same size")
        for elem in row:
            if not isinstance(elem, (int, float)) or type(matrix) is not list:
                raise TypeError(f"matrix must be a matrix "
                                f"(list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [row[:] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = round(result[i][j] / div, 2)

    return result
