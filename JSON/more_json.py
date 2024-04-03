#!/usr/bin/python3

import json

data1 = {"name": "Abel", "age": "26", "school" : "MMUST"}
data2 = '{"name": "Caleb", "age": "21", "school": "ALX"}'
data3 = {"name": "Peter", "age": "16", "school": "Chebwagan"}



with open("data3.json", "w") as f:
    json.dump(data3, f)

with open("data1.json", "w") as f:
    json.dump(data1, f)

print(json.dumps(data3))
print(json.dumps(data1, indent=4))

info = json.loads(data2)
print(info)