#!/usr/bin/python3
""" This script fetches url header using requests package """
import requests
import sys

if __name__ == '__main__':
    parameter = {"email": sys.argv[2]}
    req = requests.post(sys.argv[1], data=parameter).text
    print(req)
