
class C2:pass
class C3:pass

class C1(C2, C3):
    def __init__(self, who): # Set name when constructed
        self.name = who



class Employee:
    def computeSalary(self):
        self.salary = len(self) * 10
    def giveRaise(self):
        print(self,'has been raised')


class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


class SecondClass(FirstClass):
    def display(self):
        print('Current Value = %s' % (self.data))


class ThirdClass(SecondClass):
    def __init__(self,value):
        self.data=value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return '[ThirdClass: %s]' % self.data

    def mul(self, other):
        self.data *= other


class Person:
    def __init__(self, name, jobs, age=None): # class = data + logic
        self.name = name
        self.jobs = jobs
        self.age = age
    def info(self):
        if not age:
            return (self.name, self.jobs)
        else :return (self.name, self.jobs,self.age)    
