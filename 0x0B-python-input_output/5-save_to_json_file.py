#!/usr/bin/python3
"""
Defines The save_to_json_file function
"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    Args:
        my_obj: object to be represented
        filename: text file represent the object in JSON
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
