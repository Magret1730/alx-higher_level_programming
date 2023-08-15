#!/usr/bin/python3
import json
from os import path
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Collect command-line arguments, excluding the script name
args = argv[1:]

# Load existing content from add_item.json if it exists
if path.exists("add_item.json"):
    existing_list = load_from_json_file("add_item.json")
else:
    existing_list = []

# Add the command-line arguments to the existing list
existing_list.extend(args)

# Save the updated list to add_item.json
save_to_json_file(existing_list, "add_item.json")

# Load the updated content from add_item.json
new_list = load_from_json_file("add_item.json")
