#!/usr/bin/python3
import sys
import json
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
filename = 'add_item.json'
with open(filename, 'a+', encoding="utf-8") as f:
    if os.path.getsize(filename) != 0:
        items = load_from_json_file(filename)
        items.extend(args[1:])
        save_to_json_file(items, filename)
    else:
        items = []
        items.extend(args[1:])
        save_to_json_file(items, filename)
