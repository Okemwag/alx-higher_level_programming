#!/usr/bin/python3
"""Module for Student class."""


class Student():
    """The Student class."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dic_json = vars(self)
        if isinstance(attrs, list):
            item = {}
            for key, value in dic_json.items():
                for i in attrs:
                    if key is i:
                        item[key] = value
            return item
        else:
            return dic_json

    def reload_from_json(self, json):
        dic_json = vars(self)
        for key, value in json.items():
            dic_json[key] = value
