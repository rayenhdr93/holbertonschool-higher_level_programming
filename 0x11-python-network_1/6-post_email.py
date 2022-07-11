#!/usr/bin/python3
'''doc'''


import requests
from sys import argv


if __name__ == '__main__':
    req = requests.post(argv[1], {'email': argv[2]})
    print(req.text)
