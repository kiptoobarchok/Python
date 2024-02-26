#!/usr/bin/python3

import json

data = {
    'employee1':
    {
        "name" : 'caleb',
        'age': 21,
        'status': 'active',
        'address':
        {
            'code': '+254',
            'number': '0702171495',
            'city': 'Nairobi'
        }
    },

    'employee2':
    {
        'name': 'Abel',
        'age': 26,
        'status': 'active',
        'address':
        {
            'code': '+254',
            'city': 'kericho',
            'number':'0719507355'
        }
    }
}


new_data = json.dumps(data, indent=4)

print(new_data)