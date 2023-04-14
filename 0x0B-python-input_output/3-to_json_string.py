#!/usr/bin/python3
"""write a funcyion that returns a JSON representation of an 
object"""
import json

def to_json_string(my_obj):
    """Return tge JSON of an object(string)"""
    return (json.dump(my_obj))
