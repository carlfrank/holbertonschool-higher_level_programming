#!/usr/bin/python3
import sys

def add_arguments():
    """Add all arguments."""
    sum = 0
    for i in range(1, len(sys.argv)):
        sum += int(sys.argv[i])
    print(sum)
