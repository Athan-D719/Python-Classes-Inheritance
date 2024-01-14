#EX
###############################################################
class Point(): #class
    def __init__(self,initX,initY):
        self.x = initX #assigning instance variables
        self.y = initY

    def getX(self): #Method: belongs to the class (self) = class itself
        return self.x  #class(self).x = instance variable

    def getY(self):
        return self.y
    
    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

#INSTANCE what the class produces
point1 = Point(5,10) #<__main__.Point object>
point2 = Point(1,2) #different Point objects
               #adding parameters to the constructor
#point1.x = 5 #instance variable
#point2.x = 10 # An instance variable lives inside an instace

print(point1.getX()) # .getX = returned x = .x
     # 'self' passed to the method
#####################################################################
####################################################################
class Animal():
    def __init__(self,v1,v2):
        self.arms = v1
        self.legs = v2
    def limbs(self):
        return (self.arms + self.legs)

spider = Animal(4,4)
spidlimbs = spider.limbs()
############################################################################
########################################################################
cityNames = ['Ditroit', 'Ann Arbor', 'Pittsburgh', 'Mars', 'New York']
population = [68025, 117070, 304391, 8406000]
states = ['MI', 'MI', 'PA', 'PA', 'NY']

city_tuples - zip(cityNames, population, states)

class City:

    def __init_(self, n, p ,s):    
    self.name = n
    self.population = p
    self.state = s

    def __str__(se1f):
    return '{}, {} (pop: {})'.format(self.name, self.state, self.population)

cities = []

#for city_tup in city_tuples:
#    name, pop, state = citt_tup #tuple unpack
#    #print(name,pop,state)
#    city = City(name,pop,state) #instance of the city class
#    print(city)

cities = [City(*t) for t in city_tuples]
print(cities)
###################################################################
###################################################################
