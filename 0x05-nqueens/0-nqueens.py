#!/usr/bin/python3
""" N-queens problem module
"""

import sys


def is_safe(queens_positions, row, col):
    """
    Check if placing a queen at the specified position is safe.

    Args:
        queens_positions (list): List of queen positions
        (coordinates format [row, column]).
        row (int): Row of the position to check.
        col (int): Column of the position to check.

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    for cord in queens_positions:
        queen_row, queen_col = cord
        if (queen_col == col or
            queen_col + (row - queen_row) == col or
                queen_col - (row - queen_row) == col):
            return False
    return True


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    queen_positions = []
    solutions = []
    is_solution_found = False
    current_row = 0
    current_col = 0

    while current_row < n:
        go_back = False
        while current_col < n:
            if is_safe(queen_positions, current_row, current_col):
                queen_coordinates = [current_row, current_col]
                queen_positions.append(queen_coordinates)
                if current_row == n - 1:
                    solutions.append(queen_positions[:])
                    for cord in queen_positions:
                        if cord[1] < n - 1:
                            current_row = cord[0]
                            current_col = cord[1] + 1
                    for i in range(n - current_row):
                        queen_positions.pop()
                    if current_row == n - 1 and current_col == n:
                        queen_positions = []
                        is_solution_found = True
                    current_row -= 1
                else:
                    current_col = 0
                break
            else:
                if current_col == n - 1:
                    go_back = True
                    break
                current_col += 1

        if is_solution_found:
            break

        if go_back:
            current_row -= 1
            while current_row >= 0:
                current_col = queen_positions[current_row][1] + 1
                del queen_positions[current_row]
                if current_col < n:
                    break
                current_row -= 1
            if current_row < 0:
                break
            continue
        current_row += 1

    for solution in solutions:
        print(solution)
