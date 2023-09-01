#!/usr/bin/python3
""" A script that takes in URL, sends a request to the URL and displays
the body of the response"""
if __name__ == "__main__":
    import urllib.request
    import sys
    from urllib.error import HTTPError
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as res:
            response = res.read.decode('utf-8')
    except HTTPError as e:
        print("Error code: {}".format(e.code))
