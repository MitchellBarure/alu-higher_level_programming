#!/usr/bin/python3
"""
This module contains the definition of the Square class.
"""


class Square:
    """
    A class that defines a square by its size.
    """

    def __init__(self, size):
        """
        Initialize the square with a private instance attribute size.

        Args:
            size: The size of the square.
        """
        self.__size = size
