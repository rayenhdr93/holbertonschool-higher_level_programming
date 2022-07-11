#!/usr/bin/python3
'''doc'''


import requests
from sys import argv

if __name__ == '__main__':
    args = {'q': ""}
    if len(argv) > 1:
        args['q'] = argv[1]
    req = requests.post('http://0.0.0.0:5000/search_user', data=args)
    je = {}
    try:
        je = req.json()
        if len(je):
            print('[{}] {}'.format(je['id'], je['name']))
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
