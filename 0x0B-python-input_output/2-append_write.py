#!/usr/bin/python3
"""write a function that append a texts at the end of a file using
UTF-8 encoding format"""


def append_write(filename="", text=""):
    """Args:
append_write : append a string at the end of a file
filename (str): the name of the file
text (str): the string to append
Return:
number of characters appended"""

    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
