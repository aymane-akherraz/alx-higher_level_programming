#!/usr/bin/python3
""" Define a append_write module """


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename: a string representing the name of the file to append to
        text: a string representing the text to be written
    """

    with open(filename, 'a', encoding="utf-8") as f:
        nb_chars = f.write(text)
    return nb_chars
