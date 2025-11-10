# WRITE A CLASS NAMED AS PERSONAL WITH INFORMATION FUNCTION WITH ARGUMENT OF NAME,MAIL,MOBILE,ADDRESS
# WRITE A ANOTHER CLASS NAMED AS EDUCATIONAL WITH INFORMATION FUNCTION WITH ARGUMENT OF MARKS
# EACH SUBJECT AND PERCENTAGE INHERIT EDUCATIONAL WITH PERSONAL

class Person:
    def __init__(self,Name,Mail,Mobile,Address):
        self.Name = Name
        self.Mail = Mail
        self.Mobile = Mobile
        self.Address = Address
    def Details(self):
        print("My Name Is: ",self.Name,"\nMy Mail_Id Is: ",self.Mail,"\nMy Mobile_No Is: ",self.Mobile,"\nMy Address Is: ",self.Address)
class Education(Person):
    def __init__(self,Name,Mail,Mobile,Address,Marks,Total,Percentage):
        super().__init__(Name,Mail,Mobile,Address)
        self.Marks = Marks
        self.Total = Total
        self.Percentage = Percentage
    def Information(self):
        super().Details()
        print("My Marks Are: ",self.Marks,"\nMy Total Is: ",self.Total,"\nMy Percentage Is: ",self.Percentage)
Marks = []
Total = 0
for i in range(5):
          Element = int(input("Enter The Mark : "))
          if Element<=100:
              Marks.append(Element)
              Total+=Element
          else:
              print("Please Enter Mark <=100")
              break
Percentage = Total/len(Marks)
Obj_Details = Education("Ashif","mohammedashif605@gmail.com",9385642379,"Madurai",Marks,Total,Percentage)
Obj_Details.Information()              
    
