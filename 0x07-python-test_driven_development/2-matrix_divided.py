#!/usr/bin/python3
""" Defines a division """


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix

    Args:
        matrix: a list of lists of integers or floats,
        div: a number (integer or float)

    Returns:
        a new matrix

    Raises:
        TypeError: if the first arg is not a matrix (list of lists)
        of integers/floats
        or if a the matrix doesn't have the same size of rows
        or if div is not a number (int or float)

        ZeroDivisionError: if div is equal to 0
    """

    if (isinstance(matrix, list) and len(matrix) != 0 and
        all(isinstance(sublist, list) and len(sublist) != 0 and
            all(isinstance(el, (int, float)) for el in sublist)
            for sublist in matrix)):

        if not isinstance(div, (int, float)):
            raise TypeError('div must be a number')

        if div == 0:
            raise ZeroDivisionError('division by zero')

        ln = len(matrix[0])
        for row in matrix:
            if len(row) != ln:
                err = "Each row of the matrix must have the same size"
                raise TypeError(err)

        return [[round((e / div), 2) for e in row] for row in matrix]

    err_m = "matrix must be a matrix (list of lists) of integers/floats"
    raise TypeError(err_m)
