#!/usr/bin/python3
""" Rectangle module """


class Rectangle:
    """ Defines a rectangle """
    def __init__(self, width=0, height=0):
        """
        Constructor.

        Args:
            width: an integer representing the width of the rectangle
            height: an integer representing the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Defines a getter method for the width property

        Returns:
            the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Defines a setter method for the width property

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """
        Defines a getter method for the height property

        Returns:
            the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Defines a setter method for the height property

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value
