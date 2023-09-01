#!/usr/bin/python3
""" A script that takes a url and return the X-Request-id of the header"""
if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    res = requests.get(url)
    print(res.headers.get('X-Request-Id'))
