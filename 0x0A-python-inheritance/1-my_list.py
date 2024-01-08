#!/usr/bin/python3
""" Define a class named MyList """


class MyList(list):
    """ Define a class named MyList that inherits from list """

    def print_sorted(self):
        """ Prints the list, but sorted (ascending sort) """

        print(sorted(self))
