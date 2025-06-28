#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if the index is valid
    if idx >= 0 and idx < len(my_list):
        # Delete the element at the specified index
        del my_list[idx]

    # Return the modified list (or the original list if the index is invalid)
    return my_list
