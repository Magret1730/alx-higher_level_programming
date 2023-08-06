#!/usr/bin/python3
"""function that multiplies 2 matrices by using the module NumPy"""

import numpy as py


def lazy_matrix_mul(m_a, m_b):

    """
    Function that multiplies 2 matrices using NumPy.

    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.

    Returns:
        list: Result of matrix multiplication.
    """

    mat_1 = py.array(m_a)
    mat_2 = py.array(m_b)

    return py.dot(mat_1, mat_2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
