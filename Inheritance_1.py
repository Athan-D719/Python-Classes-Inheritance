CURRENT_YEAR = 2020
class Person:
    def __init__(self, name, year_born):
        self.name = name
        self.year_born = year_born   
    def getAge(self):
        return CURRENT_YEAR - self.year_born
    def __str__(self):
        return '{} ({})'.format(self.name, self. getAge())


class Student(Person):
    def __init__(self, name, year_born):
        Person.__init__(self,name,year_born) #calling the __init(Person)
        self.knowlegde = 0
    def study(self):
        self.knowlegde += 1

alice = Student('Alice Smith', 1990)
alice.study()
print(alice.knowlegde)
print(alice)
print(alice.getAge())
#######################################################################