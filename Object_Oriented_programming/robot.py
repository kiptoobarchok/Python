#!/usr/bin/python3


class robot:

    count = 0
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year
        self.__class__.count += 1


    def say_hi(self):
        print(f"Hi, I am {self.name}")

    

x = robot("RGDX", 2019)
y = robot("RGDX-2", 2023)

robot.brand = "AURA"
print("\n")

x.say_hi()
y.say_hi()
print("\n")

print(x.__dict__)
print(y.__dict__)

print("\n")

print(robot.__dict__)

print("\n")
print(f"{x.name} : {x.brand}")
