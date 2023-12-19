#!/usr/bin/python3
"""Defines a class MagicClass"""
import math


class MagicClass:
    """Define a circle"""
    def __init__(self, radius=0):
        """
        Constructor

        Args:
            radius: radius of the new MagicClass object.
        Raises:
            TypeError: if radius is not a number.
        """
        self.__radius = 0
        if type(self.__radius) is not int and type(self.__radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Returns the area of the new MagicClass object."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns the circumference of the new MagicClass object."""
        return 2 * math.pi * self.__radius
