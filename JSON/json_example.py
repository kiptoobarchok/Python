#!/usr/bin/python3

import json

json_str = '''
{
    "employee_info": [
        {
            "name": "Caleb",
            "status": "active",
            "age": 21,
            "id_number": 39430369,
            "email": "calebkiptoo9090@gmail.com"
        },
        {
            "name": "Abel",
            "status": "retired",
            "age": 26,
            "id_number": 39431270,
            "email": "abel5134@gmail.com"
        }
    ]
}
'''

data = json.loads(json_str)
print(data)
print('\n')
print("name: ", data['employee_info'][0]['name'])

print('\n')

data["key"] = True

new_data = json.dumps(data, indent=2)
print(new_data)