#!/usr/bin/python3
""" module for UTF-8 validation
"""


def validUTF8(data):
    """ Determines if a given data set represents a valid UTF-8 encoding
    """
    remaining_bytes = 0

    for byte in data:
        if byte & 0b11000000 == 0b10000000:
            if remaining_bytes == 0:
                return False
            remaining_bytes -= 1
        else:
            if remaining_bytes != 0:
                return False
            if byte & 0b10000000 == 0:
                remaining_bytes = 0
            elif byte & 0b11100000 == 0b11000000:
                remaining_bytes = 1
            elif byte & 0b11110000 == 0b11100000:
                remaining_bytes = 2
            elif byte & 0b11111000 == 0b11110000:
                remaining_bytes = 3
            else:
                return False

    if remaining_bytes != 0:
        return False

    return True
