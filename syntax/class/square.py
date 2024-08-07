#!/usr/bin/python3

"defining a class : square"


class Square:
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must integer")
        
        elif (size < 0):
            raise ValueError("size must be >=0")
        
        self.__size = size


    def area(self):
        return self.__size * self.__size
    
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        self.__size = value


