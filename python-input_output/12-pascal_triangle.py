#!/usr/bin/python3
"""
Module: pascal_triangle

This module provides a function to generate Pascal's triangle up to \
        the nth row.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Parameters:
        n (int): Number of rows to generate in Pascal's triangle.

    Returns:
        list of lists: Pascal's triangle represented as a list of lists \
                of integers.
                       Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row

    for i in range(1, n):
        # Create a new row in the triangle
        row = [1]  # Start with the first element

        # Fill the row with elements based on the previous row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        row.append(1)  # End with the last element
        triangle.append(row)  # Add the row to the triangle

    return triangle
