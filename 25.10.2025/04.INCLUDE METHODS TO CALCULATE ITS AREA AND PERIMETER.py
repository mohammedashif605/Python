# INCLUDE METHODS TO CALCULATE ITS AREA AND PERIMETER
# IMPLEMENT SUBCLASS FOR SHAPES LIKE CIRCLE,TRIANGLE,SQUARE
# CLASS CIRCLE
# CLASS TRIANGLE
# CLASS SQUARE
class Shape:
    pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def Area(self):
        return 3.14*self.radius*self.radius
    def Perimeter(self):
        return 2*3.14*self.radius
class Triangle(Shape):
    def __init__(self,b,h,a1,a2,a3):
        self.b = b
        self.h = h
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
    def Area(self):
        return 0.5*self.b*self.h
    def Perimeter(self):
        return self.a1+self.a2+self.a3
class Square(Shape):
    def __init__(self,a):
        self.a = a
    def Area(self):
        return self.a*self.a
    def Perimeter(self):
        return 4*self.a
Obj_Circle = Circle(7)
Obj_Triangle = Triangle(5,6,3,4,5)
Obj_Square = Square(10)
print("Circle Area: ",Obj_Circle.Area())
print("Circle Perimeter: ",Obj_Circle.Perimeter())
print("Triangle Area: ",Obj_Triangle.Area())
print("Triangle Perimeter: ",Obj_Triangle.Perimeter())
print("Square Area: ",Obj_Square.Area())
print("Square Perimeter: ",Obj_Square.Perimeter())
