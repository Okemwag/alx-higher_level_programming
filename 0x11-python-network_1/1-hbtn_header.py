#!/usr/bin/python3
"""This script reads a particular header value"""
import urllib.request as lib
import sys

if __name__ == '__main__':
    req = lib.Request(sys.argv[1])
    with lib.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
