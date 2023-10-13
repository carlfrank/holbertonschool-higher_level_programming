#!/usr/bin/python3
"""This module will have a function that will print a text"""


def text_indentation(text):
    """Prints a text, adding 2 new lines after each ., ? and :."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            if i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1
