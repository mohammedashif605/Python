# WRITE A PROGRAM TO CREATE AN ABSTRACT CLASS SHAPE WITH ABSTRACT METHODS CALCULATE AREA() AND PERIMETER()
# CREATE SUBCLASSES CIRCLE AND TRIANGLE THAT INHERIT THE SHAPE CLASS.
# AND IMPLEMENT THE RESPECTIVE METHODS TO CALCULATE THE AREA AND PERIMETER OF EACH SHAPE.

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def Area(self):
        pass
     @abstractmethod
    def Perimeter(self):
        pass
class Circle(Shape):
    def __init__(self,Radius):
        self.Radius = Radius
    def Area(self):
        return 3.14*(self.Radius**2)
    def Perimeter(self):
        return 2*3.14*self.Radius
class Triangle(Shape):
    def __init__(self,Base,Height,Side1,Side2,Side3):
         self.Base = Base
         self.Height = Height
         self.S1 = Side1
         self.S2 = Side2
         self.S3 = Side3
    def Area(self):
        return 0.5*self.Base*self.Height
    def Perimeter(self):
        return (self.S1+self.S2+self.S3)
Obj_Circle = Circle(6)
Obj_Triangle = Triangle(3,2,8,5,9)
print("Area Of Circle Is: ",Obj_Circle.Area())
print("Perimeter Of Circle Is: ",Obj_Circle.Perimeter())        
print("Area Of Triangle Is: ",Obj_Triangle.Area())    
print("Perimeter Of Triangle Is: ",Obj_Triangle.Perimeter())
