#!/usr/bin/python3
"""Square module"""


class Square:
    """Defined a square"""

    def __init__(self, size=0):
        """
        Constructor.

        Args:
            size: length of one side of the square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.

        """
        self.__size = size

    @property
    def size(self):
        """
        Defines a getter method for the size property

        Returns:
            the size of one side of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Defines a setter method for the size property

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of a square.

        Returns:
            the current square area.
        """
        return self.__size ** 2
