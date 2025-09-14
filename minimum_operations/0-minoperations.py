#!/usr/bin/python3
"""
Module to calculate minimum operations to get n H characters.
"""

def minOperations(n):
        """
            Calculate the minimum number of operations (Copy All and Paste)
                to get exactly n 'H' characters in a file.
                    
                        Args:
                                n (int): Target number of H characters.
                                        
                                            Returns:
                                                    int: Minimum number of operations, or 0 if impossible.
                                                        """
                                                            if n < 2:
                                                                        return 0  # Can't do anything for n < 2
                                                                        
                                                                        operations = 0
                                                                            divisor = 2

                                                                                while n > 1:
                                                                                            while n % divisor == 0:
                                                                                                            operations += divisor
                                                                                                                        n //= divisor
                                                                                                                                divisor += 1

                                                                                                                                    return operations

