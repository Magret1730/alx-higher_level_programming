#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return matrix
    if matrix:
        for row in matrix:
            if len(row) != len(matrix):
                return None
        return [[element ** 2 for element in row] for row in matrix]
    else:
        return matrix

# def square_matrix_simple(matrix=[]):
#    if matrix is None:
#        return None
#
#    if matrix:
#        # Verify if the matrix is square
#        for row in matrix:
#            if len(row) != len(matrix):
#                return None  # Return None if the input matrix is not square
#
#        # Create and return the square matrix
#        return [[element ** 2 for element in row] for row in matrix]
#    else:
#        return None  # Return None if the input matrix is empty
