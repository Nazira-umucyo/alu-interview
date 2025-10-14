#!/usr/bin/python3
"""
0-pascal_triangle.py
Returns a list of lists of integers representing the Pascal’s triangle of n
"""

def pascal_triangle(n):
        """
            Generate Pascal's triangle up to the nth row
                Args:
                        n (int): number of rows
                            Returns:
                                    list of lists of integers representing Pascal’s triangle
                                        """
                                            if n <= 0:
                                                    return []

                                                    triangle = [[1]]  # first row

                                                        for i in range(1, n):
                                                                    prev_row = triangle[-1]
                                                                            # Each row starts and ends with 1
                                                                                    new_row = [1]

                                                                                            # Middle values are the sum of the two numbers above it
                                                                                                    for j in range(1, len(prev_row)):
                                                                                                                    new_row.append(prev_row[j - 1] + prev_row[j])

                                                                                                                            new_row.append(1)
                                                                                                                                    triangle.append(new_row)

                                                                                                                                        return triangle
