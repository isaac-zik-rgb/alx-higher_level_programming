#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""

if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') \
         as response:
        content_string = response.read()
        content_byte = content_string.decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(content_string)))
        print("\t- content: {}".format(content_string))
        print("\t- utf8 content: {}".format(content_byte))
