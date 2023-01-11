#!/usr/bin/python3
"""Defines json file-read func.
"""
import json


def load_from_json_file(filename):
    """Create python obj from a json file.
    """
    with open(filename) as file:
        return json.load(file)
