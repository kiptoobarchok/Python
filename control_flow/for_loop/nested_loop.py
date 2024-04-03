#!/usr/bin/python3
"""
use one loop inside another loop which is called nested loop.
syntax:
        for iter_var in sequence:
            for iter_var_2 in sequence:
                statement(s)
            statement(s)
"""

for i in range(0, 9):
    for j in range(i):
        print("*", end= ' ')
    print()


for i in range(0, 5):
    j = j - 1
    for j in range(i):
        print("#", end=' ')
    print()
