#!/usr/bin/python3
""" Define Rectangle module """
from models.base import Base


class Rectangle(Base):
    """ Define a Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor.

        Args:
            width: An integer representing the width of the Rectangle
            height: An integer representing the height of the Rectangle
            x: An integer
            y: An integer
            id: An integer
        """

        self.__width = self.valid_atts("width", width)
        self.__height = self.valid_atts("height", height)
        self.__x = self.valid_atts("x", x)
        self.__y = self.valid_atts("y", y)
        super().__init__(id)

    @staticmethod
    def valid_atts(att, val):
        """
        Validates attributes

        Raises:
            TypeError: If att is not an integer
            ValueError: if width or height are under or equals 0,
            or If x or y are under 0
        """
        if not isinstance(val, int):
            raise TypeError("{} must be an integer".format(att))

        if (att == "width" or att == "height") and val <= 0:
            raise ValueError("{} must be > 0".format(att))

        if (att == 'x' or att == 'y') and val < 0:
            raise ValueError("{} must be >= 0".format(att))

        return val

    @property
    def width(self):
        """ Get/set the width of the Rectangle """

        return self.__width

    @width.setter
    def width(self, value):

        self.__width = self.valid_atts("width", value)

    @property
    def height(self):
        """ Get/set the height of the Rectangle """

        return self.__height

    @height.setter
    def height(self, value):

        self.__height = self.valid_atts("height", value)

    @property
    def x(self):
        """ Get/set the x attribute """

        return self.__x

    @x.setter
    def x(self, value):

        self.__x = self.valid_atts("x", value)

    @property
    def y(self):
        """ Get/set the y attribute """

        return self.__y

    @y.setter
    def y(self, value):

        self.__y = self.valid_atts("y", value)

    def area(self):
        """ Returns the area value of the Rectangle instance """

        return self.__width * self.__height

    def display(self):
        """ Prints in stdout the Rectangle instance with the character # """

        print("\n" * self.__y, end="") if self.__y > 0 else None

        for i in range(self.height):
            print(" " * self.__x, end="") if self.__x > 0 else None
            print("#" * self.__width)

    def __str__(self):
        """ Returns [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        id = self.id
        x = self.__x
        y = self.__y
        width = self.__width
        height = self.__height

        return "[Rectangle] ({}) {}/{} - {}/{}".format(id, x, y, width, height)

    def update(self, *args, **kwargs):
        """
            Assigns an argument to each attribute or
            assigns a key/value argument to attributes

        Args:
            args: A no-keyword argument
            kwargs: A key-worded argument
        """

        ln = len(args)
        if args is not None and ln != 0:
            my_list = ['id', 'width', 'height', 'x', 'y']
            for i in range(ln):
                setattr(self, my_list[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle """

        my_dict = {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y,
        }

        return my_dict
