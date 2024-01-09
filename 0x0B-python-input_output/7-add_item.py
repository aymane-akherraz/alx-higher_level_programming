#!/usr/bin/python3
""" Define a JSON decoding module """
import json
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
my_list = []

if os.path.exists(filename):
    my_list = load_from_json_file(filename)

args = sys.argv

for i in range(1, len(args)):
    my_list.append(args[i])

save_to_json_file(my_list, filename)
