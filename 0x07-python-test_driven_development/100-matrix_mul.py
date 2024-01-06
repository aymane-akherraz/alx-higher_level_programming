#!/usr/bin/python3
""" Defines a Matrix multiplication """


def matrix_mul(m_a, m_b):
    """ Multiplies 2 matrices

    Args:
        m_a: first matrix
        m_b: second matrix

    Raises:
        TypeError: m_a is not a list or m_b is not a list or
            if m_a or m_b is not a list of lists or
            if m_a or m_b is not a rectangle (all rows should be
            of the same size)
        ValueError: if m_a or m_b is empty or if m_a and m_b
        can't be multiplied

    Returns:
        A new matrix representing the multiplication of m_a by m_b
    """

    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    if not all(isinstance(sublist, list) for sublist in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isinstance(sublist, list) for sublist in m_b):
        raise TypeError('m_b must be a list of lists')

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for el in m_a:
        for item in el:
            if not isinstance(item, (int, float)):
                raise TypeError('m_a should contain only integers or floats')
    for el in m_b:
        for item in el:
            if not isinstance(item, (int, float)):
                raise TypeError('m_b should contain only integers or floats')

    ln = len(m_a[0])
    if not all(len(row) == ln for row in m_a):
        raise TypeError('each row of m_a must be of the same size')
    ln = len(m_b[0])
    if not all(len(row) == ln for row in m_b):
        raise TypeError('each row of m_b must be of the same size')

    ln = len(m_b)
    if len(m_a[0]) != ln:
        raise ValueError("m_a and m_b can't be multiplied")

    new = []
    r = 0
    for i in range(len(m_a)):
        new += [[]]
        for j in range(ln):
            for k in range(len(m_b[j])):
                r += m_a[i][k] * m_b[k][j]
            new[i].append(r)
            r = 0
    return new
