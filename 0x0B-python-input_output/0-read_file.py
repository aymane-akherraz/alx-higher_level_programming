#!/usr/bin/python3
""" Define a read_file module """


def read_file(filename=""):
    """ Reads a text file (UTF8) and prints it to stdout
    Args:
        filename: a string representing the name of the file to read from
    """

    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
