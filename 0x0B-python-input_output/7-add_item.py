#!/usr/bin/python3
"""
script to save and load
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item,json'
arglist = list(sys.argv[1:])

try:
    data = load_from_json_file(filename)
except Exception:
    data = []

data.extend(arglist)
save_to_json_file(data, filename)
