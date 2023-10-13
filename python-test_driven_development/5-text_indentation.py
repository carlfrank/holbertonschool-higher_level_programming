#!/usr/bin/python3
"""This module will have a function that will print a text"""


def text_indentation(text):
    """Print a text, adding 2 new lines after each ., ? and :."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_characters = ['.', '?', ':']
    for char in special_characters:
        text = text.replace(char, char + '\n\n')
    lines = text.split('\n')
    for line in lines:
        print(line.strip())
