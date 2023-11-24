#!/usr/bin/python3


class email:
    def __init__(self, f_name, l_name):
        self.__f_name = f_name
        self.__l_name = l_name
    
    @property
    def f_name(self):
        return self.__f_name

    @property
    def l_name(self):
        return self.__l_name

    @f_name.getter
    def f_name(self):
        return self.__f_name
    
    @f_name.setter
    def f_name(self, name):
        if isinstance(name, int):
            raise TypeError("name can't have an integer")
        self.__f_name = name

    @l_name.setter
    def l_name(self, name):
        if isinstance(name, int):
            raise TypeError("name can't have an integer")
        self.__l_name = name


    @l_name.getter
    def l_name(self):
        return self.__l_name
    
    def my_email(self):
        return (f"{self.__f_name}{self.__l_name}@gmail.com")


a = email("Caleb99", "kiptoo")
print(a.my_email())