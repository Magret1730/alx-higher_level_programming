#!/usr/bin/python3
"""A function"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n
    """

    if n <= 0:
        return []

    pascal_list = [[1]]  # Initialize with the first row

    for _ in range(1, n):  # Generate the next n-1 rows
        prev_row = pascal_list[-1]  # Get the last row

        new_row = [1]  # First element of the new row

        for i in range(1, len(prev_row)):
            new_value = prev_row[i - 1] + prev_row[i]
            new_row.append(new_value)

        new_row.append(1)  # Last element of the new row

        pascal_list.append(new_row)

    return pascal_list
