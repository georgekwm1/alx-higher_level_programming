#!/usr/bin/python3
"""Defines the number of '#' to print"""

def print_square(size):
    """
    This function adds two integers.

    Args:
    size (int): number of '#' to print.
    
    Returns:
    Prints '#' based on the number specified.
    """
    symbol = "#"
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == None:
        raise ValueError("Input an Integer")
    for i in range(size):
        print("{}".format(symbol * size), end='\n')
