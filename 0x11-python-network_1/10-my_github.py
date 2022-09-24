#!/usr/bin/python3
""" Uses Basic Authentication to get id from Github API
"""
if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    from sys import argv

    r = requests.get('https://api.github.com/user',
                     auth=HTTPBasicAuth(argv[1], argv[2]))
    if r.status_code is not 200:
        print("None")
    else:
        data = r.json()
        print(data.get("id"))
