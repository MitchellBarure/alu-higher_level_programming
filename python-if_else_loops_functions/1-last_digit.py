#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Get the last digit
last_digit = abs(number) % 10

# If the number is negative, adjust the last digit to be negative
if number < 0:
    last_digit = -last_digit

# Construct the output message
message = f"Last digit of {number} is {last_digit} and is "

if last_digit > 5:
    message += "greater than 5"
elif last_digit == 0:
    message += "0"
else:
    message += "less than 6 and not 0"

print(message)
