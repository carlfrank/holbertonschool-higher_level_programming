#!/usr/bin/python3
"""This module will have a function that will print a text"""


def text_indentation(text):
    """Indent text."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    new_text = ""
    for char in text:
        new_text += char
        if char in special_chars:
            new_text += '\n\n'

    lines = new_text.split('\n')
    for line in lines:
        print(line.strip())
