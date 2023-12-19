#!/usr/bin/python3
"""Square module"""


class Square:
    """Defined a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Constructor.

        Args:
            size: length of one side of the square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.

        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Defines a getter method for the position property

        Returns:
            the size of one side of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Defines a setter method for the position property

        Raises:
            TypeError: if it's not a tuple of 2 positive integers.
        """
        if (type(value) is not tuple or len(value) != 2 or
                type(value[0]) is not int or type(value[1]) is not int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of a square.

        Returns:
            the current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""

        s = self.__size
        if s == 0:
            print()
        else:
            for e in range(self.__position[1]):
                print()
            for i in range(s):
                for k in range(self.__position[0]):
                    print(" ", end="")
                print("#" * s)
