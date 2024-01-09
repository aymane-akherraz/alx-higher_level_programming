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

    if hasattr(obj, name):
        raise TypeError("can't add new attribute")
    setattr(obj, name, val)
