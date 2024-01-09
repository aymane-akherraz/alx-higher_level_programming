#!/usr/bin/python3
""" Define a JSON decoding module """
import json


def load_from_json_file(filename):
    """ Creates an Object from a “JSON file”

    Args:
        filename: A string representing the name of the file to read from
    """

    with open(filename, 'r', encoding="utf-8") as f:
        my_obj = json.load(f)
    return my_obj
