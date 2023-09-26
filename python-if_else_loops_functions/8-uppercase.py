#!/usr/bin/python3
def uppercase(input_str):
    result = ""
    for char in input_str:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            result += uppercase_char
        else:
            result += char
    print(result)
