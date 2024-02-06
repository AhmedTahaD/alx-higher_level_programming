#!/usr/bin/python3
"""
script to save and load
"""
import sys
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

a = []
if path.exists("add_item.json"):
    a = load_from_json_file("add_item.json")
a = a + argv[1:]
save_to_json_file(a, "add_item.json")
