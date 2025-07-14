#!/usr/bin/python3
"""
Inserts a line of text into a file after each line containing \
        a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Reads a file, inserts new_string after lines with search_string, \
            then overwrites the file.
    """
    # Read all lines from the file
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Build new content, inserting new_string after lines with search_string
    new_content = []
    for line in lines:
        new_content.append(line)
        if search_string in line:
            new_content.append(new_string)

    # Write the modified content back to the file
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(new_content)
