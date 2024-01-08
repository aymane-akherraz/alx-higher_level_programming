#!/usr/bin/python3
""" Defines a function called inherits_from"""


def inherits_from(obj, a_class):
    """
    Returns if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class

    Args:
        obj: An object
        a_class: A class

    Returns:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class ; otherwise False.
    """
    return (isinstance(obj, a_class) and (type(obj) != a_class))
