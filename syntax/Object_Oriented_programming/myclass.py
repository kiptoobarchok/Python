#!/usr/bin/python3

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"
    
    def greet(self):
        print(f"Hi {self.name} , how're u doin")



person1 = person(input("enter name : "), input("\nage : "))
# person1.age = 28
print(person1.__str__())

person1.greet()

# del person1.age

print(person1.age)

