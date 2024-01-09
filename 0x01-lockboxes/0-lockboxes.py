#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
    - boxes (list of lists): Each box is numbered sequentially from 0 to n - 1,
    and each box may contain keys to the other boxes.

    Returns:
    - bool: True if all boxes can be opened, else return False.
    """

    is_visited = [False] * len(boxes)
    is_visited[0] = True
    box_stack = [0]

    while box_stack:
        current_box_index = box_stack.pop()
        for key in boxes[current_box_index]:
            if not is_visited[key]:
                is_visited[key] = True
                box_stack.append(key)

    return all(is_visited)
