# simple class syntax

class Robot:
    def __init__(self, name, buildYear, work, ai=False):
        self.__name = name
        self.__buildYear = buildYear
        self.__ai = ai
        self.__work = work

    def set_name(self, name):
        if self.__name:
            print(f"Hi , I am {self.__name}")

    def get_name(self):
        return self.__name
    
a = Robot('RGDX', 2003, "Data-Retriver", True)
print(a.get_name())
print(a.__dict__)

