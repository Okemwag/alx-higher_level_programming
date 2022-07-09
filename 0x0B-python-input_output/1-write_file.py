#!/usr/bin/python3
"""Module for number_of_lines function."""


def write_file(filename="", text=""):
    """This function writes a string to  file overwrites if exist."""
    with open(filename, mode='w', encoding='utf-8') as f:
        len = f.write(text)

    return len
