# WRITE A PYTHON PROGRAM TO CREATE A CLASS REPRESENTING CIRCLE.
# INCLUDE METHODS TO CALCULATE ITS AREA AND PERIMETER
# CLASS CIRCLE : AREA(R) PERIMETER(R)

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius*self.radius
    def perimeter(self):
        return 2*3.14*self.radius
Obj_Circle = Circle(10)
print("The Area Of Circle Is : ",Obj_Circle.area())
print("The Perimeter Of Circle Is : ",Obj_Circle.perimeter())
