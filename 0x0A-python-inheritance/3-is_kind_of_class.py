#!/usr/bin/python3
""" Defines a function called is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """
    Returns if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class

    Args:
        obj: An object
        a_class: A class

    Returns:
        True if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class, otherwise False.
    """
    return (isinstance(obj, a_class))
