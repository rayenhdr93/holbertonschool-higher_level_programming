#!/usr/bin/python3
'''doc'''


import requests
from sys import argv


if __name__ == '__main__':
    req = requests.get("https://api.github.com/user", auth=(argv[1], argv[2]))
    try:
        print(req.json()['id'])
    except KeyError:
        print(None)
