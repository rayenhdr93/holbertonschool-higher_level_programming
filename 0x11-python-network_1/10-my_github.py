#!/usr/bin/python3
'''doc'''


import requests
from sys import argv


if __name__ == '__main__':
    req = requests.get(
        'https://api.github.com/users/{}'.format(argv[1]),
        auth=(argv[1], argv[2]))
    print(req.json()['id'])
