#!/usr/bin/python3

import json

# person = '{"name": "Bob", "languages": ["English", "French"]}'
# person_dict = json.loads(person)

# # Output: {'name': 'Bob', 'languages': ['English', 'French']}
# print( person_dict)

# # Output: ['English', 'French']
# print(person_dict['languages'])

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "courses": ["Math", "Science"],
    "address": {
        "street": "123 Main St",
        "zipcode": "10001"
    }
}

to_json = json.dumps(data, indent=4)

print(to_json)
file_path = 'johnDoe.json'

with open(file_path, 'w') as file:
    file.write(to_json)
print(f"file data copied successfully to : {file_path}")

print(type(to_json))