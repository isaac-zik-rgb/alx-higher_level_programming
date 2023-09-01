#!/usr/bin/python3
""" Takes in a `URL`, sends a request to th `URL` and display the value
of the X-Request"""

if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        response = res.headers['X-Request-Id']
        print(response)
