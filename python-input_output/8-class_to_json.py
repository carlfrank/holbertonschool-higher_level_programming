#!/usr/bin/python3
"""Module to create a class from JSON file"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.
    """
    return {key: value for key, value in obj.__dict__.items()}
