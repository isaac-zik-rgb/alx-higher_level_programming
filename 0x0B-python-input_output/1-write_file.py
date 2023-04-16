#!/usr/bin/python3
"""Define a function that writes test to a file"""


def write_file(filename="", text=""):
    """Args:
write_file: create a file and writes on the file
filename (obj): the name of the file to be created
text : the texts to be writen on the file
Returns:
total number of texts in a file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
