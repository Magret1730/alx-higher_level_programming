def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            i = 0  # Reset i for each new row
            for element in row:
                print("{:d}".format(element), end=" ")
                i += 1
            print()
