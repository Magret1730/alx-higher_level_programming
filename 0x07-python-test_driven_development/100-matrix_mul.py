#!/usr/bin/python3
"""
function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """function multiplies two matrices"""

    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError('m_a must be a list of lists')
        if len(row) != len(m_a[0]):
            raise TypeError('each row of m_a must be of the same size')
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError('m_a should contain only integers or floats')
    for rows in m_b:
        if not isinstance(rows, list):
            raise TypeError('m_b must be a list of lists')
        if len(rows) != len(m_b[0]):
            raise TypeError('each row of m_b must be of the same size')
        for values in rows:
            if not isinstance(values, (int, float)):
                raise TypeError('m_b should contain only integers or floats')
    if len(m_a) == 0:
        raise ValueError("m_a and m_b can't be multiplied")
    if len(m_b) == 0:
        raise ValueError("m_a and m_b can't be multiplied")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(element)
        result.append(row)
    return result
