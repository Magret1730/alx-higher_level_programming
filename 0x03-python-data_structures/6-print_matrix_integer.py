#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        j = 0
        for row in matrix:
            i = 0  # Reset i for each new row
            for element in row:
                print("{:d}".format(matrix[j][i]), end=" ")
                i += 1
            print()
            j += 1 
