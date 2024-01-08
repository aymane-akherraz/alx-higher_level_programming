#!/usr/bin/python3
""" Defines a function called lookup"""


def lookup(obj):
    """
    A function that returns the list of available
    attributes and methods of an object

    Args:
        obj: An object
    Returns:
        A list object
    """
    return dir(obj)
