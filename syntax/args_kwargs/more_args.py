#!/usr/bin/python3

"pizza party"

def pizza(*slices):
    for i in slices:
        print(f"eating a {i} slice ")


def order_pizza(**toppings):
    for topping , amount in toppings.items():
        print("Adding", amount, topping, "to the pizza")
