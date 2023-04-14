#!/usr/bin/python3
"""write a fuction that writes an object to a text file"""

import json


def save_to_json_file(my_obj, filename):
    """write an obect to a text file using json"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dumps(my_obj, f)
