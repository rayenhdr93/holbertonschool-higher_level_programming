#!/usr/bin/python3
'''doc'''

import requests


if __name__ == '__main__':
    req = requests.get('https://intranet.hbtn.io/status')
    html = req.text
    print("Body response:\n\t- type: {}\n\t- content: {}".format(
        type(html), html))
