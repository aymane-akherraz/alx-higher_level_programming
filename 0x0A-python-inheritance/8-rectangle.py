#!/usr/bin/python3
""" Defines a Rectangle Module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Defines a Rectangle class that inherits from BaseGeometry """

    def __init__(self, width, height):
        """
        Constructor.

        Args:
            width: an integer representing the width of the rectangle
            height: an integer representing the height of the rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
