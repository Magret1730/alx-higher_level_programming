#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # if len(matrix) != 0:
    if matrix is not None:
        j = 0
        for row in matrix:
            i = 0
            for column in row:
                print("{:d}".format(matrix[j][i]), end=" ")
                i += 1
            print()
            j += 1
