#!/usr/bin/python3

"""
continue statement in python: 
        used to skip the rest of the statements in the current loop

break statement:
        stops execution of a looping statement
"""

while True:
    s = input("Enter string: ")
    if s == 'exit' or s == 'quit':
        break

    if len(s) < 3:
        print('Too small')
        continue

    print('Input is of sufficient length')
    