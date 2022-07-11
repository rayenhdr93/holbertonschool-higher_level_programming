#!/usr/bin/python3
'''doc'''


from urllib import request
from sys import argv
from urllib.error import HTTPError


if __name__ == '__main__':
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
