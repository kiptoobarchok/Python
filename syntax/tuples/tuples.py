#!/usr/bin/env python3

'tuples are immutable'

myTuple = [1, 2, 3, 4, 5]
print(type(myTuple))

#change list to tuple
print(type(tuple(myTuple)))

mySecTuple = ('caleb', 'abel', 'peter', 'kevin')
print(type(mySecTuple))