#!/usr/bin/python3
""" This script posts email address to server"""
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    mail = {"email": sys.argv[2]}
    encoded = urllib.parse.urlencode(mail).encode("ascii")

    request = urllib.request.Request(sys.argv[1], encoded)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
