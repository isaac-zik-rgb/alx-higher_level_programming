#!/usr/bin/python3
"""Define a function that reads file and print it out on stdout"""


def read_file(filename=""):
    """Args:
read_file - read texts from a file
filename (str): the file to read it from
Return:
Nothing"""

    with open("filename", encoding="utf=8") as f:
        print(f.read())
