#!/usr/bin/python3
"""
while loop is used to execute a block of statements repeatedly
until a given condition is satisfied. When the condition becomes false,
the line immediately after the loop in the program is executed.
"""

count = input("enter number ro start: ")
num = int(count)

while (num < 3):
    num += 1 #'without this the loop is infinite'
    print("Hello Caleb")


"""
while loop can also be used with else statement
    syntax:
        while condition:
            statement to execute
        else:
            statement to execute after exiting while block
"""



while True:
    age = int(input("Enter your age:- "))
    if (age >= 18):
        print("You are a voter")
    else:
        print("you are still an underage in kenya")
