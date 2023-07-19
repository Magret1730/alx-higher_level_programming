#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        print()
    if matrix is not None:
        # for row in matrix: if len(row) != len(matrix): return matrix
        return [[element ** 2 for element in row] for row in matrix]
    else:
        return matrix
