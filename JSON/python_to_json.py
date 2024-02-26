#!/usr/bin/python3


import json

x = {
    "f_name": "Kiptoo",
    "l_name": "Caleb",
    "age": 21,
    "city": "Nairobi",
    "address": {
        "Box": "00511",
        "Home": "Ongata Rongai",
        "Lane": "Gate 6"
    }
}

data = json.dumps(x, indent=4, sort_keys=True)

print(data)

print("\n")

print(json.dumps({"Name": "John", "Age": 30}, indent=2))
