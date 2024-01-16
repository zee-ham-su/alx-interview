#!/usr/bin/env python3
"""
Minimum Operations interview question
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in
    exactly n H characters in a file.
    """
    characters_in_file = 1
    clipboard = 0
    operations_count = 0

    while characters_in_file < n:
        operations_count += 1 if clipboard == 0 else 0
        clipboard = characters_in_file if clipboard == 0 else clipboard

        remaining_chars = n - characters_in_file

        if remaining_chars < clipboard:
            return 0

        if remaining_chars % characters_in_file != 0:
            characters_in_file += clipboard
            operations_count += 1
        else:
            clipboard = characters_in_file
            characters_in_file += clipboard
            operations_count += 2

    return (operations_count if characters_in_file == n else 0)
