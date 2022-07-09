#!/usr/bin/python3
"""Module for from_json_string function."""
import json


def from_json_string(my_str):
    """This function returns an object represented by a JSON string."""
    return json.loads(my_str)
