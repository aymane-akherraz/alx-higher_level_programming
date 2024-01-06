#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """ Adds 2 integers and returns the result

    Args:
        a: The first integer.
        b: The second integer. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or a float.
    """
    if not type(a) in (int, float):
        raise TypeError('a must be an integer')
    if not type(b) in (int, float):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
