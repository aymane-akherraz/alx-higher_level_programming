#!/usr/bin/python3
""" Define a write_file module """


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and
    returns the number of characters written

    Args:
        filename: a string representing the name of the file to write to
        text: a string representing the text to be written
    """

    with open(filename, 'w', encoding="utf-8") as f:
        nb_chars = f.write(text)
    return nb_chars
