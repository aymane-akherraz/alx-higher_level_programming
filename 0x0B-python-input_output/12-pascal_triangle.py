#!/usr/bin/python3
""" Define a pascal_triangle module """


def pascal_triangle(n):
    """ Returns a list of lists of integers representing
    the Pascal's triangle of n

    Args:
        n: An integer
    Returns:
        an empty list if n <= 0 otherwise a list of lists of integers
        representing the Pascal's triangle of n
    """

    if n <= 0:
        return []

    m = [[1]]
    for i in range(1, n):
        m.append([])
        for j in range(i + 1):
            if j == 0 or j == i:
                m[i].append(1)
            else:
                m[i].append(m[i - 1][j] + m[i - 1][j - 1])
    return m
