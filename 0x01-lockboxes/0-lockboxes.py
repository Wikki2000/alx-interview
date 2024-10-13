#!/usr/bin/python3
"""
0-lockboxes.py
"""


def canUnlockAll(boxes):
    """unlock a box using key"""
    unlock_keys = [i for i in range(1, len(boxes))]

    attempted_key = set()

    for box in boxes:
        for key in box:
            if key in unlock_keys:
                attempted_key.add(key)
                break
    return unlock_keys == list(attempted_key)
