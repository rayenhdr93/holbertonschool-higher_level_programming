#!/usr/bin/python3
'''doc'''


import urllib.request


def test():
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:\n\t- type: {}\
\n\t- content: {}\n\t- utf8 content: {}".format(
            type(html), html, html.decode("utf-8")))


if __name__ == "__main__":
    test()
