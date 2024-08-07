#!/usr/bin/env python3

"defining a class (Square)"
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

        
        
    def area(self):
        return self.__size * self.__size
    
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        
        if (value < 0):
            raise ValueError("size must be greater than 0")
        
        else:
            self.__size = value

    def my_print(self):
        if self.__size < 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple) or
                    len(value) != 2 or 
                    not all(isinstance(num, int) for num in value) or
                    not all(num >= 0 for num in value)):

            raise TypeError("position must be a tuple of 2 positive integers")
        
        self.__position = value