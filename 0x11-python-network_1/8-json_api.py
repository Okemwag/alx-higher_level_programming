#!/usr/bin/python3
""" This sript posts a blog and validates it """
import requests
from sys import argv


if __name__ == "__main__":
    q = argv[1] if len(argv) > 1 else ""
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}
    try:
        sent = requests.post(url, data=data).json()
        if 'id' in sent and 'name' in sent:
            print("[{}] {}".format(sent['id'], sent['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
