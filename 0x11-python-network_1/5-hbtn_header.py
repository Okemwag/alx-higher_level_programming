#!/usr/bin/python3
""" Fetches website info, displays value of X-Request-Id variable in header
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
