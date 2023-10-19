#!/usr/bin/python3
"""Script that adds all arguments to a Python list"""


import sys
import os.path
import json


filename = "add_item.json"
if os.path.isfile(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []
for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])
save_to_json_file(my_list, filename)
