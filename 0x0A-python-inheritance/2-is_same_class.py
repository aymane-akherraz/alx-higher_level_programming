#!/usr/bin/python3
""" Defines a function called is_same_class"""


def is_same_class(obj, a_class):
    """
    Returns if the object is exactly an instance of the specified class

    Args:
        obj: An object
        a_class: A class

    Returns:
        True if the object is exactly an instance of the specified class,
        otherwise False.
    """

    return (type(obj) == a_class)
