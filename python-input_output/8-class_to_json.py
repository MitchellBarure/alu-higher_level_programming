#!/usr/bin/python3
"""
This module provides functions for JSON serialization and deserialization
of Python objects.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.
    """
    return obj.__dict__
