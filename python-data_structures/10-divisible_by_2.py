#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Initialize an empty list to store the results
    result_list = []

    # Iterate through the original list
    for num in my_list:
        # Check if the number is divisible by 2
        if num % 2 == 0:
            result_list.append(True)
        else:
            result_list.append(False)

    # Return the new list with True or False values
    return result_list
