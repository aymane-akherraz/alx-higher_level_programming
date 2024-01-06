#!/usr/bin/python3
""" Defines a function that prints a square with the character #. """


def print_square(size):
    """ Prints a square with the character #

    Args:
        size: the size length of the square

    Raises:
        TypeError: If size is not an integer
        ValueError: If size < 0
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        print("#" * size)
