#!/usr/bin/python3
""" Define a JSON representation module """
import json


def save_to_json_file(my_obj, filename):
    """ Writes an Object to a text file, using a JSON representation

    Args:
        my_obj: An object
        filename: A string representing the name of the file to write to
    """

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
