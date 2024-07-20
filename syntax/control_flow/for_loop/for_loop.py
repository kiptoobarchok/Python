#!/usr/bin/python3
"""
for loops are used for sequential traversal
    ie traversing a list, string or array
syntax:
        for (iterator_variable) in sequence:
                statement(s)
"""

name = input("Enter your name: ")
for i in name:
    print(i)

"""
it can also be used in iterating over range
ie :
"""
num = 5
for i in range(0, num):
    print(i)

"""
Use case in a list
"""

myList = ['Abel', 'Caleb', 'Peter']

for i in myList:
    print(i)


"""
In list for loop can also be used to index
"""

list2 = ['a', 'b', 'c', 'd', 'e']

for i in range(len(list2)):
    print(i, ":", list2[i])