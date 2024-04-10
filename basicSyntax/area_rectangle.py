#!/usr/bin/python3

a = int(input('Enter the length: '))
b = int(input('Enter the width: '))

area = a * b

print(f"The area of the said rectangle is: {area}")

perimeter = 2 * (a + b)
print(f'The perimeter of the reactangle is: {perimeter}')


def areaFunction(c, d):
    return f'{c * d}'

area_two = areaFunction(4, 3)
print(f'finding area using a function: {area_two}')

