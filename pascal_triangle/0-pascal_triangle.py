#!/usr/bin/python3
"""
Module: 0-pascal_triangle
This module contains a single function, pascal_triangle(n),
which returns a list of lists of integers representing the
Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """
    Generates Pascal’s Triangle up to the nth row.

    Args:
        n (int): The number of rows of Pascal’s Triangle to generate.

    Returns:
        list: A list of lists of integers representing the Pascal’s Triangle.
              Returns an empty list if n <= 0.

    Example:
        >>> pascal_triangle(5)
        [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
    """
    if n <= 0:
        return []

    triangle = [[1]]  # The first row of Pascal's Triangle

    # Build each subsequent row
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # Every row starts with 1

        # Compute inner elements by summing two elements above
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)  # Every row ends with 1
        triangle.append(new_row)

    return triangle
