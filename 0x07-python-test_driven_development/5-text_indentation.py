#!/usr/bin/python3
""" Defines a function that prints a text with 2 new lines
after some characters """


def text_indentation(text):
    """ Prints a text with 2 new lines after each of these
    characters: ., ? and :

    Args:
        text: a string representing the text to be indented

    Raises:
        TypeError: If text is not a string

    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    b = 0
    for c in text:
        if c == ' ' and b == 1:
            continue
        if c in ['.', '?', ':']:
            print(c, end="\n\n")
            b = 1

        else:
            print(c, end="")
            b = 0
