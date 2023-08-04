#!/usr/bin/python3
"""
function that divides all elements of a matrix

function that divides all elements of a matrix with an int or float
"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix
    returns divided number rounded to two decimal places
    """
    if not isinstance(matrix, list) or\
            not all(isinstance(row, list) for row in matrix):
        a = "matrix must be a matrix (list of lists) "
        b = "of integers/floats"
        raise TypeError(a + b)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not all(isinstance(element, (int, float))
               for row in matrix for element in row):
        a = "matrix must be a matrix (list of lists) "
        b = "of integers/floats"
        raise TypeError(a + b)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) for element in row]
                  for row in matrix]

    return new_matrix
