#!/usr/bin/python3
""" Define a file module """


def append_after(filename="", search_string="", new_string=""):
    """ Inserts a line of text to a file,
    after each line containing a specific string

    Args:
        filename: A string representing the filename to update
        search_string: a string representing the string to search for
        new_string: a string representing the new line to be inserted
    """
    with open(filename, 'r+', encoding="utf-8") as f:
        lines = f.readlines()

        for i in range(len(lines)):
            if search_string in lines[i]:
                lines.insert(i + 1, new_string)

        f.seek(0)
        f.writelines(lines)
