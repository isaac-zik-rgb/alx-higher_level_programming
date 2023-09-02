#!/usr/bin/python3
"""script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a paramete"""
if __name__ == "__main__":
    import sys
    import requests
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    req = requests.post(url, data=data)
    print(req.text)
