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

    s = ""
    for c in text:
        s += c
        if c in ['.', '?', ':']:
            s = s.strip()
            s += "\n\n"
            print(s, end="")
            s = ""

    s = s.strip()
    print(s, end="")
