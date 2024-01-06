#!/usr/bin/python3
""" Defines a function that prints a name """


def say_my_name(first_name, last_name=""):
    """ Prints My name is <first name> <last name>

    Args:
        first_name: a string representing the first_name
        last_name: a string representing the last_name. Defaults to ""

    Raises:
        TypeError: If one of the arguments is not a string
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print("My name is {} {}".format(first_name, last_name))
