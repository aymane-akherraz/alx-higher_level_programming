#!/usr/bin/python3
""" Rectangle module """


class Rectangle:
    """ Defines a rectangle """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Constructor.

        Args:
            width: an integer representing the width of the rectangle
            height: an integer representing the height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """
            Prints the message Bye rectangle...
            when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    def __str__(self):
        """ Print the rectangle with the character # """

        str = ""
        if self.__width == 0 or self.__height == 0:
            return str

        h = self.__height
        for i in range(h):
            str += "#" * self.__width + ("\n" if i != (h - 1) else "")
        return str

    def __repr__(self):
        """ Return a string representation of the rectangle
            to be able to recreate a new instance by using eval()
        """

        return "Rectangle({}, {})".format(self.__width, self.__height)

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

    def area(self):
        """ Returns the rectangle area """

        return self.__width * self.__height

    def perimeter(self):
        """ Returns the rectangle perimeter """

        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)
