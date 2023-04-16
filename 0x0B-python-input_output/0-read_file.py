#!/usr/bin/python3
"""Define a function that reads file and print it out on stdout"""


def read_file(filename=""):
    """prints the contents of a file in a UTF-8 format"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
