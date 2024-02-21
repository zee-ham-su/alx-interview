#!/usr/bin/env python3
""" rotating a 2D matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """ rotates a 2D matrix 90 degrees clockwise"""
    num_rows = len(matrix)
    for layer in range(num_rows // 2):
        start_row = layer
        end_row = num_rows - 1 - layer
        for row_index in range(start_row, end_row):
            offset = row_index - start_row
            top_element = matrix[start_row][row_index]

            matrix[start_row][row_index] = matrix[end_row -
                                                  offset][start_row]
            matrix[end_row -
                   offset][start_row] = matrix[end_row][end_row - offset]
            matrix[end_row][end_row -
                            offset] = matrix[row_index][end_row]
            matrix[row_index][end_row] = top_element
    return matrix
