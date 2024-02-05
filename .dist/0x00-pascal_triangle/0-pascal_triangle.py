#!/usr/bin/python3
""" a python script that generate Pascal's triangle
up to the specified number of rows.
"""


def pascal_triangle(num_rows):
    """
    Generate Pascal's triangle up to the specified number of rows.

    Args:
        num_rows (int): The number of rows for Pascal's triangle.

    Returns:
        list of lists: A list of lists representing Pascal's triangle.
    """
    if num_rows <= 0:
        return []

    triangle = [[1]]

    for i in range(1, num_rows):
        new_row = [1]

        for j in range(1, i):
            new_row.append(triangle[i-1][j-1] + triangle[i-1][j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
