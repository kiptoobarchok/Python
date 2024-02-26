#!/usr/bin/python3

num = [1, 2, 3, 4, 5]
print(num)
"Unpacking in python"
print(*num)

"""
print(f"Order a {size} piza with toppings as follows: ")
use of * in variable arguements
"""

def order_pizza(size, *toppings, **details):
    print(f"order *{size}* pizza with this toppings: {toppings}")
    
    print("\nDetails of the order are: ")
    for key, value in details.items():
        print(f"-  {key} : {value}")

order_pizza("large", "cheese", 'pepperoni', 'olive', address_delivery="Kahawa Wendani", tip=False)
    
def say_hi(*args, **kwargs):
    print(f"Hello {args}")
    print(kwargs)

say_hi("caleb", "abel", 'peter')
say_hi(caleb=21, abel=26, peter=16)