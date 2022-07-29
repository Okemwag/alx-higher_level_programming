#!/usr/bin/python3
""" This script requests error code and print it"""
import sys
import urllib.error
import urllib.request

if __name__ == '__main__':
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as web:
            print(web.read().decode("ascii"))

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
