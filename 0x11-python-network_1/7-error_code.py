#!/usr/bin/python3
""" This script handles error code """
import requests
from sys import argv

if __name__ == '__main__':
    req = requests.get(argv[1])
    code = req.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(req.text)
