#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # Check if the index is within the valid range
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list
