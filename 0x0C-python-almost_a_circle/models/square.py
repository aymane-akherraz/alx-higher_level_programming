#!/usr/bin/python3
""" Define Square module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines a Square """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor.

        Args:
            size: An integer representing the size of the Square
            x: An integer
            y: An integer
            id: An integer
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Return [Square] (<id>) <x>/<y> - <size> """

        id = self.id
        x = self.x
        y = self.y
        size = self.width
        return "[Square] ({}) {}/{} - {}".format(id, x, y, size)

    @property
    def size(self):
        """ Get/Set the size of the square """

        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Assigns new values to attributes

         Args:
            args: A no-keyword argument
            kwargs: A key-worded argument
        """

        if args is not None and len(args) != 0:
            my_list = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if my_list[i] == "size":
                    setattr(self, "width", args[i])
                    setattr(self, "haight", args[i])
                else:
                    setattr(self, my_list[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """

        my_dict = {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y,
        }

        return my_dict
