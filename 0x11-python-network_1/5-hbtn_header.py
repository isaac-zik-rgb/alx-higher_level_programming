#!/usr/bin/python3
""" A script that takes a url and return the X-Request-id of the header"""
from security import safe_requests

if __name__ == "__main__":
    import sys

    url = sys.argv[1]
    res = safe_requests.get(url)
    print(res.headers.get('X-Request-Id'))
