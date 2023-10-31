#!/usr/bin/python3
"""Definition of a function that print names"""

def say_my_name(first_name, last_name=""):
    """
    This function Prints firstname and last name.

    Args:
    first_name (string): First name.
    last_name (string): Last name.

    Returns:
    Prints first name and last name.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if not first_name and not last_name:
        raise SyntaxError("Input at least one name")
    print("My name is {} {}".format(first_name, last_name))