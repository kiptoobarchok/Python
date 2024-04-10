#!/usr/bin/python3

"functions to operate all mathematical operations"

a = int(input("Enter num 1: "))
b = int(input("Enter num 2: "))

def add(a, b):
    'return sum of two nums'
    return f'Sum:\n\t{a} + {b} = {a + b}'

def mul(a, b):
    'return multiplication'
    print(f"Multiplication:\n\t{a} * {b} = {a * b}")

def div(a, b):
    return f'Division:\n\t{a} / {b} = {a / b}'

def mod(a, b):
    'return modulus / reminder'
    return f'Modulus:\n\t{a} % {b} = {a % b}'
    
def sqr(a, b):
    return f'square:\n\t{a} ** {b} = {a ** b}'

d = {a /b}
m = {a % b}
rem = d - m
print(f'remainder from division: {rem}')

print(add(a, b))
print(mul(a, b))
print(div(a, b))
print(mod(a, b))
print(sqr(a, b))

