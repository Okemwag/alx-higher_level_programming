#!/usr/bin/python3
""" Fetches website info, handles urllib.error.HTTPError exceptions
"""
if __name__ == "__main__":
    from urllib import request, error
    from sys import argv

    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as e:
        if e.reason == "UNAUTHORIZED":
            print("Error code: 401")
        elif e.reason == "NOT FOUND":
            print("Error code: 404")
        elif e.reason == "INTERNAL SERVER ERROR":
            print("Error code: 500")
