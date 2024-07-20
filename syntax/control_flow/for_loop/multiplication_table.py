#!/usr/bin/python3

"""
using nested loops to create a multiplication table of upto 10
"""

for i in range(1, 10):
    for j in range(1, 10):
        print(i, "*" , j ," = ", i * j)
    print()
