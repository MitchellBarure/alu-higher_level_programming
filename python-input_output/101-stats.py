#!/usr/bin/python3
"""
Reads log data from stdin, computes metrics, and prints stats \
        every 10 lines or on CTRL+C.
"""

import sys


def print_statistics(total_size, status_codes):
    """Prints total file size and status code counts, sorted by code."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


total_file_size = 0
status_codes_count = {}
line_count = 0
possible_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Ensure there are enough parts before attempting to access
        if len(parts) < 2:
            continue  # Skip lines that don't even have a status code and \
                    file size

        try:
            # Extract status code and file size from the end of the list
            status_code_str = parts[-2]
            file_size_str = parts[-1]

            status_code = int(status_code_str)
            file_size = int(file_size_str)

        except (ValueError, IndexError):
            continue  # Skip lines if status_code or file_size cannot be \
                    converted to int

        total_file_size += file_size

        if status_code in possible_status_codes:
            status_codes_count[status_code] = status_codes_count.get \
                    (status_code, 0) + 1

        if line_count % 10 == 0:
            print_statistics(total_file_size, status_codes_count)

except KeyboardInterrupt:
    pass

finally:
    print_statistics(total_file_size, status_codes_count)
