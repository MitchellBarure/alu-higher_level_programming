#!/usr/bin/python3
"""
This module provides a function to read a text file (UTF8) \
        and print its content to stdout.

Function:
    read_file(filename=""): Reads the content of the specified \
            file and prints it to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read. \
                Default is an empty string.
"""
    with open(filename, "r", encoding="utf-8") as file:
        Noel = file.read()
        print(Noel, end="")
