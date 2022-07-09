#!/usr/bin/python3
"""
Add all arguments to a Python list, and then save them to a file
"""


import json
import sys


save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'

try:
    f = load_file(filename)
except:
    f = []

for args in sys.argv[1:]:
    f.append(args)

save_file(f, filename)
