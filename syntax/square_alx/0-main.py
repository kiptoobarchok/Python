#!/usr/bin/env python3

Square = __import__('square').Square

# my_square = Square(2)
# print(type(my_square))
# print(my_square.__dict__)
# print("********************************")
# try:
#     my_square2 = Square(-3)
#     print(my_square2.__dict__)
# except Exception as e:
#     print(e)

# print("********************************")

# try:
#     my_square3 = Square(4)
#     print(f"the area ot ur square is: {my_square3.area()}")
# except Exception as e:
#     print(e)
# print("********************************")

my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)

print("********************************")

my_square4 = Square(3)
my_square4.my_print()

print("********************************")

my_square5 = Square(9, (3, 4))
my_square5.my_print()

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
print("********************************")
s_5 = Square(5)
s_6 = Square(6)

if s_5 < s_6:
    print("Square 5 < Square 6")
if s_5 <= s_6:
    print("Square 5 <= Square 6")
if s_5 == s_6:
    print("Square 5 == Square 6")
if s_5 != s_6:
    print("Square 5 != Square 6")
if s_5 > s_6:
    print("Square 5 > Square 6")
if s_5 >= s_6:
    print("Square 5 >= Square 6")