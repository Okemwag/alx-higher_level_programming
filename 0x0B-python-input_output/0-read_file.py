#!/usr/bin/python3
"""Module for read_file method."""


def read_file(filename=""):
    """Read a file."""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
