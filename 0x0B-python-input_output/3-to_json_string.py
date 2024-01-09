#!/usr/bin/python3
""" Define a JSON representation module """
import json


def to_json_string(my_obj):
    """ Returns the JSON representation of an object (string)

    Args:
        my_obj: An object
    """

    return json.dumps(my_obj)
