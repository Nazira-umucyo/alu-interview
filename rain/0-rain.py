#!/usr/bin/python3
"""
0-rain.py
Calculate the total amount of rainwater retained between walls.
"""


def rain(walls):
        """
            Calculate how many square units of water will be retained after it rains.

                Args:
                            walls (list): A list of non-negative integers representing wall heights.

                                Returns:
                                        int: Total amount of rainwater retained.

                                            Example:
                                                        >>> rain([0, 1, 0, 2, 0, 3, 0, 4])
                                                                6
                                                                    """
                                                                        if not walls:
                                                                                    return 0

                                                                                    length = len(walls)
                                                                                        water = 0

                                                                                            # Create lists to store the maximum height to the left and right of each index
                                                                                                left_max = [0] * length
                                                                                                    right_max = [0] * length

                                                                                                        # Fill left_max array
                                                                                                            left_max[0] = walls[0]
                                                                                                                for i in range(1, length):
                                                                                                                            left_max[i] = max(left_max[i - 1], walls[i])

                                                                                                                                # Fill right_max array
                                                                                                                                    right_max[-1] = walls[-1]
                                                                                                                                        for i in range(length - 2, -1, -1):
                                                                                                                                                    right_max[i] = max(right_max[i + 1], walls[i])

                                                                                                                                                        # Calculate trapped water at each index
                                                                                                                                                            for i in range(length):
                                                                                                                                                                        water += min(left_max[i], right_max[i]) - walls[i]

                                                                                                                                                                            return water
