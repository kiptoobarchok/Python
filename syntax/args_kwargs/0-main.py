#!/usr/bin/python3

# pizza = __import__('more_args').pizza
# # pzz = __import__('more_args').order_pizza

# pizza1 = pizza("cheese")
# print(pizza1)

# pizza2 = pizza("pepperoni", "crusted")
# print(pizza2)

# # pizza3 = order_pizza(a=1, b=2)
# # print(pizza3)

thisdict = {"name": "caleb",
        "age": 21,
        "contact": "0702171495",
        "role": "developer"
        }

for col_i , col_ii in thisdict.items():
    print(f"{col_i} : {col_ii}")


print(thisdict["role"])

thisdict["id"]=39430369

print(thisdict)

del thisdict["age"]

print(thisdict)