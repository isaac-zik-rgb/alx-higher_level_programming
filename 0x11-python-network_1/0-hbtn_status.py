#!/usr/bin/python3
""" A script that fetches a uri and disply its body"""
if __name__ == "__main__":
    import urlib.request
    """import request from urllib libary"""
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content_string = response.read()
        content_byte = content_byte.decode()
        print("Body response:")
        print("\t - type: {}".format(content_string))
        print("\t - content: {}".format(content_string))
        print("\t - utf8 content: {}".format(content_byte))
        
