#!/usr/bin/python3
""" Sends POST request to URL with email as a parameter
"""
if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv

    data = {}
    data['email'] = argv[2]
    post = parse.urlencode(data)
    post = post.encode('ascii')
    req = request.Request(argv[1], post)
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
