#!/usr/bin/python3
""" Print the pascal numbers. """


def pascal_triangle(n):
    """ Handle the core algorithm of pascal triangle. """

    if n <= 0:
        return []

    triangle = [[1]]  # First row always assign to 1

    # Iterate from row index 1
    for i in range(1, n):
        row = [1]  # Pascal triangle starts with 1

        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        row.append(1)  # Last item ends with one

        triangle.append(row)

    return triangle
