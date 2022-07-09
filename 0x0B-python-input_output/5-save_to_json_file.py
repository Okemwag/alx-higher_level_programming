#!/usr/bin/python3
"""Module for save_to_json function."""
import json


def save_to_json_file(my_obj, filename):
    """This function writes an Object to a text file."""
    with open(filename, "w") as f:
        return json.dump(my_obj, f)
