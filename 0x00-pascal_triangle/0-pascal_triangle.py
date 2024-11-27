#!/usr/bin/python3
"""
0-pascal_triangle.py
"""


def pascal_triangle(n):
    """
    Creates pascale trinagle
    """
    if n <= 0:
        return []

    pascal_array = [[] for i in range(n)]

    for i in range(n):
        if i == 0:
            pascal_array[i].append(1)
            continue

        for j in range(i + 1):
            up_left = pascal_array[i - 1][j - 1] if j != 0 else 0
            up_right = pascal_array[i - 1][j] if j != i else 0
            pascal_array[i].append(up_left + up_right)

    return pascal_array
