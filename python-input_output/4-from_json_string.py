#!/usr/bin/python3
""" task 3 """
import json


def from_json_string(my_str):
    """ returns an object (Python) represented by a JSON string """
    return json.loads(my_str)
