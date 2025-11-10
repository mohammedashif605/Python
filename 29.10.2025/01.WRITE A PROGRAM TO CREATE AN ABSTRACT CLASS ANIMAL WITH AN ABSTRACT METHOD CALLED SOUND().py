# WRITE A PROGRAM TO CREATE AN ABSTRACT CLASS ANIMAL WITH AN ABSTRACT METHOD CALLED SOUND()
# CREATE SUBCLASS LION AND TIGER THAT INHERIT THE ANIMAL CLASS
# AND IMPLEMENT THE SOUND() METHOD TO MAKE A SPECIFIC SOUND FOR EACH ANIMAL.

from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def Sound(self):
        pass
class Lion(Animal):
    def Details(self):
        print("My Name Is Lion")
    def Sound(self):
        print("Lion Is Roar")
class Tiger(Animal):
    def Details(self):
        print("My Name Is Tiger")
    def Sound(self):
        print("Tiger Is Roaring")
Obj_Lion = Lion()
Obj_Lion.Sound()
Obj_Tiger = Tiger()
Obj_Tiger.Sound()
