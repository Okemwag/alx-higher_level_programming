#!/usr/bin/python3
""" This script displays github commits and authors """
import requests
from sys import argv

if __name__ == '__main__':
    github = "https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1])

    res = requests.get(github)
    commits = res.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
