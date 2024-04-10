#!/usr/bin/python3

'''
python program to check if a number is a prime number

'''

num = int(input("Enter the number you want to check if it is a prime number:\n\t\t"))

#check if number can be divided by another number other than itself
#use a number that we know is not a prime number
#other_num = num / 5

'''
if other_num != 0:
    print(f'This {num} is a prime number\nThis was confirmed by testing using division :\
          \nthe number {num} / 5 , which is known not to be  a prime number\n \
            \nHence the expected output is non-zero')
    
'''

###

class my_math:
    def is_prime(num):
        if num <= 1:
            print(f'{num} is not a prime number')
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print(f'{num} is not a prime number')
        print(f'{num} is a prime number')


