#!/usr/bin/python3

myModel = __import__('base_model').BaseModel()

myModel.name = 'caleb'
myModel.number = 9090

print(myModel)
print(myModel.save())
myjson = myModel.to_dict()
print(myjson)

for key in myjson.keys():
    print("\t{}: ({}) - {}".format(key, type(myjson[key]), myjson[key]))