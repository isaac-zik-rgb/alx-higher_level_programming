#!/usr/bin/python3
"""Defines a string-to-JSON function"""
import json


def to_json_string(my_obj):
    """Return the JSON of an object(string)"""
    return (json.dumps(my_obj))
