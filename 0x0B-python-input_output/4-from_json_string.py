#!/usr/bin/python3
""" Define a JSON decoding module """
import json


def from_json_string(my_str):
    """ Returns an object (Python data structure) represented by a JSON string

    Args:
        my_str: A JSON string
    """

    return json.loads(my_str)
