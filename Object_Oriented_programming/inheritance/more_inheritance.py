#!/usr/bin/python3


class info:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f"Hello, I am {self.name}")


class student(info):
    def __init__(self, name, adm, id):
        super().__init__(name)
        self.adm = adm
        self.id = id

    def details(self):
        print(f"name: {self.name}\nID: {self.id}\nADM: {self.adm}")

class teacher(info):
    def __init__(self, name, id, work_no):
        super().__init__(name)
        self.id  = id
        self.work_no = work_no

    def details(self):
        print(f"name : {self.name}\nID: {self.id}\nWork number: {self.work_no}")

p1 = student("caleb", "E37/2579", 39430369)
p1.details()

p2 = teacher("Abel", 3366902, "B/A-5134")
p2.details()

print(p1.__dict__)