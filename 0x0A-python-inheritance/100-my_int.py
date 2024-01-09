#!/usr/bin/python3
""" Defines MyInt  Module"""


class MyInt(int):
    """ Define a class MyInt inherits from int """

    def __eq__(self, other):
        """Rich comparison operator to compare if an integer is not
        equal to another.

        Args:
            other (integer): integer to compare self to.

        Returns: True or false
        """
        return int(self) != int(other)

    def __ne__(self, other):
        """Rich comparison operator to compare if integer is
        equal to another.

        Args:
            other (integer): integer to compare self to.

        Returns: True or false
        """
        return int(self) == int(other)
