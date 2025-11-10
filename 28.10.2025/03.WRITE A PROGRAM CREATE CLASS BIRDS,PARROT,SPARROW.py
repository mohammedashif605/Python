# WRITE A PROGRAM CREATE CLASS BIRDS,PARROT,SPARROW.
# DESCRIBE THE BIRD NAME IS CONSTRUCTOR
# DESCRIBE THE BIRDS SOUND IN MAKE_SOUND FUNCTION

class Bird:
    def __init__(self,Name):
        self.Name = Name
    def Make_Sound(self):
        print(self.Name,"Makes a Sound")
class Parrot(Bird):
    def Make_Sound(self):
        print(self.Name,"Screeching")
class Sparrow(Bird):
    def Make_Sound(self):
        print(self.Name,"Chirping")
Obj_Parrot = Parrot("Parrot")
Obj_Sparrow = Sparrow("Sparrow")
Obj_Parrot.Make_Sound()
Obj_Sparrow.Make_Sound()
        
