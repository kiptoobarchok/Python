#!/usr/bin/python3

"""
work out the age of the user
"""
x = int(input("Enter the year you were born : "))

age = (2024 - x)

print(age)

if age <= 0:
    print("Invalid!!\nEnter the year again: ")
    
elif age < 18:
    print("You are not yet of age in Kenya")
else:
    print("You're now an adult")
