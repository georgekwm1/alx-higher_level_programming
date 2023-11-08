#!/usr/bin/python3
# 6-from_json_string.py
"""Definition of a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string.
    Args:
        my_str (str): A valid JSON string.
        
    Returns:
    """
    return json.loads(my_str)
