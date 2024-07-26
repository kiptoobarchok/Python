#!/usr/bin/env python3

import json

file_path = './johnDoe.json'


with open(file_path, 'r') as file:
    ld_data = json.load(file)

print(ld_data)
print(type(ld_data))