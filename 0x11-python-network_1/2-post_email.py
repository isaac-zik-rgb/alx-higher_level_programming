#!/usr/bin/python3
""" Script that takes in a URL and an email, sends a POST request
to the passed URL with the email and display the response"""

if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        response = res.read()
        print(response.decode('utf-8'))
