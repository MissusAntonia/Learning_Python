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


class Manager:
    def __init__(self,name,pay):
        self.person = Person(name,'mgr',pay)
    def giveRaise(self,percentage,bonus=10):
        self.person.giveRaise(percentage+ bonus)
    def __getattr__(self, attr):
        return getattr(self.person, attr) # Delegate all other attrs
    def __repr__(self):
        return str(self.person)



if __name__ == '__main__':
    import sys
    mouktar= Person('Sulyman Mouktar')
    antu = Person('Kinteh Antonia', job='Teacher',pay= 150000)
    print(mouktar.name,mouktar.pay)
    print(antu.name, antu.pay)
    print(mouktar.name.split()[-1]) # Extract object's last name
    antu.pay *= 1.10             # Give this object a raise
    print('%.2f' % antu.pay)
    print(mouktar.lastName(),antu.lastName())

    tola=Person('Alade Tola','Pry_Teacher',10000)

    print(tola.name, tola.pay)
    q=10
    print("Increment Tola's Pay by %s" % (q))
    tola.giveRaise(q)
    print(tola.name,tola.pay)
    print(mouktar,type(mouktar))
    tom= Manager('Oyewale Jones', 50000) # Make a Manager: __init__
    tom.giveRaise(10)
    print(tom.name)# Runs custom version
    print(tom.lastName()) # Runs inherited method
    print(tom),print(type(tom))
    print('--All three--')
    for obj in (mouktar,antu,tom):
        obj.giveRaise(10)
        print(obj)
    zee = Manager('Sulyman Zainab',20000)

    print(zee.job)
