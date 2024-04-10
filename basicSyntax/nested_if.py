#!/usr/bin/python3

num = int(input("Enter your guess number: "))

if num > 0 and num <= 10:
    if (num  == 5):
        print('I am 5, Hurray!!')
    else:
        print('I am other, not sad face')
else:
    print('I am waaay bigger!!')
