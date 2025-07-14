#!/usr/bin/python3
"""
This module contains a function that creates an Object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file.

    Args:
        filename (str): The name of the file from which the object will be /
        loaded.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
