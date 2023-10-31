#!/usr/bin/python3
"""Definition of the addition function"""

def add_integer(a, b=98):
    """
    This function adds two integers.

    Args:
    a (int): First integer.
    b (int, optional): Second integer. Defaults to 98.

    Returns:
    int: Sum of the integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    
    return int(a) + int(b)
