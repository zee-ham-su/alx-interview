#!/usr/bin/python3
"""
Minimum Operations interview question
"""


def minOperations(n):
    """Determines the minimum number of operations required
    to achieve exactly target_chars 'H' characters in this file
    """
    clipboard = 0
    current_chars = 1
    operations_counter = 0

    while current_chars < n:
        if clipboard == 0:
            clipboard = current_chars
            operations_counter += 1
        if current_chars == 1:
            current_chars += clipboard
            operations_counter += 1
            continue

        remaining = n - current_chars
        if remaining < clipboard:
            return 0

        if remaining % current_chars != 0:
            current_chars += clipboard
            operations_counter += 1
        else:
            clipboard = current_chars
            current_chars += clipboard
            operations_counter += 2

    return (operations_counter if current_chars == n else 0)
