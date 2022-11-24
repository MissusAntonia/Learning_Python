from __future__ import print_function
class Person:
    """docstring fo Person."""

    def __init__(self,name,job=None,pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def giveRaise(self,percentage):
        x=percentage/10
        self.pay=int(self.pay*(10+x)/10)

    def lastName(self):
        return self.name.split()[0]

    def __repr__(self):
        return f'[Person:{self.name},{self.pay}]'

class Manager(Person):
    def __init__(self,name,pay):
        Person.__init__(self,name,'mgr',pay)

    def giveRaise(self,percentage,bonus=10):
        Person.giveRaise(self,percentage +bonus)


class Department:
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, person):
        self.members.append(person)
    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    tom = Manager('Tom Jones', 50000)
    development = Department(bob, sue) # Embed objects in a composite
    development.addMember(tom)
    development.giveRaises(.10) # Runs embedded objects' giveRaise
    development.showAll() # Runs embedded objects' __repr__                 
