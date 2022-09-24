#!/usr/bin/python3
""" Fetches website info using urllib library
"""
if __name__ == "__main__":
    from urllib import request
    print("Body response:")
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        print("\t- type: {}".format(type(response.read())))
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        print("\t- content: {}".format(response.read()))
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        print("\t- utf8 content: {}".format(response.read().decode("utf-8")))
