#!/usr/bin/python3
"""
script to save and load
"""
import sys
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'
my_list = list(sys.argv[1:])
try:
    old_data = load_from_json_file(filename)
except Exception:
    old_data = []

old_data.extend(my_list)
save_to_json_file(old_data, filename)
