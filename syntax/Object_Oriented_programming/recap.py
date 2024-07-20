#!/usr/bin/python3


class person:
    def __init__(self):
        pass

    def name(self, name):
        self.name = name

    def name(self):
        return self.name


a = person()
a.name = ("Caleb Kiptoo")

print(a.name)
