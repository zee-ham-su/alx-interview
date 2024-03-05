#!/usr/bin/python3
""" island perimeter
"""


def island_perimeter(grid) -> int:
    """ function that returns the perimeter of the island
    """
    total_perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                total_perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    total_perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    total_perimeter -= 2
    return total_perimeter
