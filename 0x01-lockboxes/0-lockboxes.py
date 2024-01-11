#!/usr/bin/python3
"""a method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
    - boxes (list of lists): Each box is numbered sequentially from 0 to n - 1,
    and each box may contain keys to the other boxes.

    Returns:
    - bool: True if all boxes can be opened, else return False.
    """
    length = len(boxes)
    is_visited = set()
    box_stack = [0]

    while box_stack:
        current_box_index = box_stack.pop()
        is_visited.add(current_box_index)

        for key in boxes[current_box_index]:
            if key != 0 and key < length and key not in is_visited:
                box_stack.append(key)

    return all(box in is_visited for box in range(length))
