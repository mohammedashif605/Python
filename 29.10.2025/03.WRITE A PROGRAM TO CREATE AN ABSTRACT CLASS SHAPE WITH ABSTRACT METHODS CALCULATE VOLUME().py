# WRITE A PROGRAM TO CREATE AN ABSTRACT CLASS SHAPE WITH ABSTRACT METHODS CALCULATE VOLUME()
# CREATE SUBCLASSES CYLINDER,CONE,SPHERE THAT INHERIT THE SHAPE CLASS.
# AND IMPLEMENT THE RESPECTIVE METHODS TO CALCULATE VOLUME OF EACH SHAPE.

from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def Volume(self):
        pass
class Cylinder(Shape):
    def __init__(self,Radius,Height):
        self.Radius = Radius
        self.Height = Height
    def Volume(self):
        return 3.14*(self.Radius**2)*self.Height
class Cone(Shape):
    def __init__(self,Radius,Height):
        self.Radius = Radius
        self.Height = Height
    def Volume(self):
        return (1/3)*3.14*(self.Radius**2)*self.Height
class Sphere(Shape):
    def __init__(self,Radius,Height):
        self.Radius = Radius
        self.Height = Height
    def Volume(self):
        return (4/3)*3.14*(self.Radius**3)*self.Height
Obj_Cylinder = Cylinder(1,2)
print("Volume Of Cylinder Is: ",Obj_Cylinder.Volume())
Obj_Cone = Cone(1,2)
print("Volume Of Cone Is: ",Obj_Cone.Volume())
Obj_Sphere = Sphere(1,2)
print("Volume Of Sphere Is: ",Obj_Sphere.Volume())
