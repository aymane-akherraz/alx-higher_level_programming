#!/usr/bin/python3
""" Defines a BaseGeometry Module"""


def add_attribute(obj, name, val):
    """
    Adds a new attribute to an object if it's possible

    Args:

        obj: an object
        name: the name of the attribute
        val: the value of the attribute

    Raises:
        TypeError: if the object can't have new attribute
    """

    if not hasattr(obj, "__dict__") or hasattr(obj, name) or \
            hasattr(obj, "__slots__") and name not in obj.__slots__:
        raise TypeError("can't add new attribute")

    setattr(obj, name, val)
