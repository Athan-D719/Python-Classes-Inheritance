class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self): #conversion to actual value.
        return "x = {}, y = {}".format(self.x, self.y)

p = Point(7,6)
print(p)
####################################################################################################
#####################################################################
class Cereal:
    def __init__(self,str1,str2,int3):
        self.name = str1
        self.brand = str2
        self.fiber = int3
    def __str__(self):
        return "{} cereal is produced by {} and has {} grams of fiber in every serving!".format(self.name, self.brand, self.fiber)
    
c1 = Cereal("Corn Flakes","Kellogg's", 2)
c2 = Cereal("Honey Nut Cheerios","General Mills", 3)
print(c1)
print(c2)
####################################################################
#################################################################
