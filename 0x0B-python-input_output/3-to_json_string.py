#!/usr/bin/python3
"""Defines The to_json_string function"""


import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)
    Args:
        my_obj(str): a string param

    Return: the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
