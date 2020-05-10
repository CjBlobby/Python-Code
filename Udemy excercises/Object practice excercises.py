import math


class Line:

    def __init__(self, coord1, coord2):
        self.coord1 = coord1
        self.coord2 = coord2

    def length(self):
        x = self.coord1[0] - self.coord2[0]
        y = self.coord1[1] - self.coord2[1]
        length = math.sqrt(x ** 2 + y ** 2)
        return length

    def grad(self):
        run = self.coord1[0] - self.coord2[0]
        rise = self.coord1[1] - self.coord2[1]
        return rise / run

class Cylinder:

    pi = 3.14159

    def __init__(self, height, radius):

        self.height = height
        self.radius = radius


    def volume(self):

        return Cylinder.pi * self.radius**2 * self.height

    def area(self):

        base = Cylinder.pi * self.radius ** 2
        circumference = Cylinder.pi * self.radius * 2

        return 2*base + circumference*self.height


#mycan = Cylinder(2, 3)
#print(mycan.volume(),"\t", mycan.area())



#myline = Line((3, 2), (8, 10))
#print(myline.length())
#print(myline.grad())




        
