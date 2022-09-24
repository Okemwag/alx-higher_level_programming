#!/usr/bin/python3
""" Fetches website info, displays value of X-Request-Id variable in header
"""
if __name__ == "__main__":
    from urllib import request
    from sys import argv

    with request.urlopen(argv[1]) as response:
        print(response.info())
        # header = dict(response.info())
        # print(header.get("X-Request-Id"))
