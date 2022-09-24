#!/usr/bin/python3
""" Fetches website info using requests (must be installed)
"""
if __name__ == "__main__":
    import requests
    print("Body response:")
    r = requests.get('https://intranet.hbtn.io/status')
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
