#!/usr/bin/python3
'''LockBoxes Challenge'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    '''
    num_boxes = len(boxes)
    box_keys = set()
    visited_boxes = []
    current_box_index = 0

    while current_box_index < num_boxes:
        old_box_index = current_box_index
        visited_boxes.append(current_box_index)
        box_keys.update(boxes[current_box_index])

        for key in box_keys:
            if key != 0 and key < num_boxes and key not in visited_boxes:
                current_box_index = key
                break

        if old_box_index == current_box_index:
            break

    if any(i not in visited_boxes and i != 0 for i in range(1, num_boxes)):
        return False
    else:
        return True
