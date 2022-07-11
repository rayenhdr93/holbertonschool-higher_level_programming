#!/usr/bin/python3
'''doc'''


from urllib import request, parse
from sys import argv


if __name__ == '__main__':
    args = parse.urlencode({'email': argv[2]}).encode('utf-8')
    with request.urlopen(argv[1], args) as response:
        print(response.read().decode('utf-8'))
