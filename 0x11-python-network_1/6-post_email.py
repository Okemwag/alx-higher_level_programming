#!/usr/bin/python3
""" Sends POST request to URL with email as a parameter
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    data = {}
    data['email'] = argv[2]
    post = requests.post(argv[1], data)
    print(post.text)
