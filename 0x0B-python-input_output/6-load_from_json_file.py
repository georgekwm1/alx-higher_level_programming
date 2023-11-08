#!/usr/bin/python3
"""Definition of a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file.
    Args:
        filename (str): The name and path to the JSON file.
        
    Returns:
    """
    with open(filename) as f:
        return json.load(f)
