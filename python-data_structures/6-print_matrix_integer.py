#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, value in enumerate(row):
            if i < len(row) - 1:
                print("{:d}".format(value), end=" ")
            else:
                print("{:d}".format(value), end="")
        print()  # Move to the next line after each row
