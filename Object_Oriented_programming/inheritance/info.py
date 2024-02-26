#!/usr/bin/pyhton3


class person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def print_name(self):
        print(f"{self.firstname} {self.lastname}")

class occupation(person):
    def __init__(self, firstname, lastname, title):
        super().__init__(firstname, lastname)
        self.title = title

    def job(self):
        print(f"{self.firstname} {self.lastname} is a {self.title}")


p1 = occupation("Kiptoo", "Caleb", "Software engineer")
p2 = occupation("Abel", "Kiprob", "Teacher")


p1.print_name()
p2.print_name()
p2.job()