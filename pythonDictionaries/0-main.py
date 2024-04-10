#!/usr/bin/python3

'test robotDict file'

import sys

from robotDict import myRobotDict
from dict_constructor import secondRobotDict

if __name__ == '__main__':
    print(f"Name : {myRobotDict['name']}")

    #overwrite value 
    myRobotDict["name"] = "RGDX_2.0"

    print(f"Name : {myRobotDict['name']}")

    print(type(myRobotDict))

    #print the all dictionary
    #with the updated changes ie name changed
    print(myRobotDict)

    #check number of items in dictionary
    print(f"Number of items in my dict : {len(myRobotDict)}")


    "Using the dict() constructor"
    print(secondRobotDict)

    print(f"second robot Name : {secondRobotDict['name']}")


    # Accessing dictionary items
    first_robot = myRobotDict['name']
    print(f"my first robot : {first_robot}")

    #using get() method
    second_robot = secondRobotDict.get("name")
    print(f"My second robot: {second_robot}")

    #keys() - this returns all keys in the dictionary
    print(myRobotDict.keys())
    print(myRobotDict.values)

    # values() - this returns all values
    print(secondRobotDict.keys())
    print(secondRobotDict.values())


    #items() returns the items of the dictionary as tuples in a list
    print(secondRobotDict.items())
    
