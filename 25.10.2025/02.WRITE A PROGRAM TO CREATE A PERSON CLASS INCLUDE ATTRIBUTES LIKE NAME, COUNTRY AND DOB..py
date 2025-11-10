# WRITE A PROGRAM TO CREATE A PERSON CLASS INCLUDE ATTRIBUTES LIKE NAME, COUNTRY AND DOB.
# IMPLEMENT A METHOD TO DETERMINE THE PERSON'S AGE.

from datetime import date
class Person:
    def __init__(self,Name,Country,Dob):
        self.Name = Name
        self.Country = Country
        self.Dob = Dob
    def Age(self):
        today = date.today()
        Age = today.year - self.Dob.year
        if (today.month,today.day) < (self.Dob.month,self.Dob.day):
            age-=1
        return Age
Obj_Person = Person("Ashif","India",date(2002,4,26))
print("Name Is : ",Obj_Person.Name,"\nCountry Is : ",Obj_Person.Country,"\nDate Of Birth Is : ",Obj_Person.Dob)
print("Age Is",Obj_Person.Age())

        
