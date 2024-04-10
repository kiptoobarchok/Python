#!/usr/bin/python3

'test robotDict file'

import sys

from robotDict import myRobotDict

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

