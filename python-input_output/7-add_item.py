#!/usr/bin/python3
""" task 7 """
from sys import argv
from os import path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if path.exists('add_item.json'):
    item_list = load_from_json_file('add_item.json')
else:
    item_list = []
for i in range(1, len(argv)):
    item_list.append(argv[i])
save_to_json_file(item_list, 'add_item.json')
