#!/usr/bin/python3
"""
simple class to encapsulate a robots attributes
"""
import time


class Robot:
    '''
    class attribute
    shared by all the instances of the class
    '''
    count = 0
    brand = 'AURA'
    #initializing the class with two instance attributes
    def __init__(self):

        Robot.count += 1

    #method to set name
    def set_name(self, value=None):
        self.__name = value
        return value

    #get name method
    def get_name(self):
        return self.__name
    
    #method to set build year and its getter
    def set_buildYr(self, value):
        self.__buildYear = value

    def get_buildYr(self):
        return self.__buildYear
    
    #make the robot to greet person on launch
    def say_hi(self):
        if self.__name:
            print(f'Hello there, I am {self.__name}\nWhat do you want to know about me')
        else:
            print(f'Hello, I am a robot with no name\nPerhaps you can name me')
            user_input = a.set_name(input("Enter your robot's name: "))
            print(f"Nice name, now i'll be called {user_input}.")

    

if __name__ == "__main__":
    a = Robot()
    a.set_name("RGDX")
    a.set_buildYr(2003)
    print(a.get_name())
    a.say_hi()
    print(a.__dict__)
    print(a.brand)


    b = Robot()
    b.set_name("RGDX-2.0")
    b.set_buildYr(2013)
    print(b.__dict__)
    print(f'Total robots: {Robot.count}')
