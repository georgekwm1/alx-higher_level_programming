#!/usr/bin/python3
"""Definition of a text indentation function"""

def text_indentation(text):
    """
    This function indents a text.

    Args:
    a (str): Text to be indented.

    Returns:
    Prints indented Text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        print(char, end='')
        if char in (".", "?", ":"):
            print("\n\n", end='')
