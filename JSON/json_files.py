#!/usr/bin/python3

import json

data = {

    "student1":
    {
        "name": 'Caleb',
        'age': 21,
        'school': 'Alx',
        'adm': "E37/2579",
        'address':
        {
            'zipcode': '00511',
            'city': 'Ongata Rongai',
            'TelNo.': '0702171495'
        }
    },

    'student2':
    {
        "name": 'Abel',
        'age': 26,
        'school': 'MMUST',
        'adm': "A01/5134",
        'address':
        {
            'zipcode': '001100',
            'city': 'Kericho',
            'TelNo.': '0719507355'
        }
    }
}

json_data = json.dumps(data, indent=2)
print(json_data)