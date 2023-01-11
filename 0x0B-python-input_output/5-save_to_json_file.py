#!/usr/bin/python3
"""Defines json file-writing func.
"""
import json


def save_to_json_file(my_obj, filename):
    """Write object to txt file using json rep.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
