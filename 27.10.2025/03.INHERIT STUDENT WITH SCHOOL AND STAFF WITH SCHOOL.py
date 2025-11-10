# WRITE A PYTHON CLASS NAMED AS SCHOOL WITH INFORMATION FUNTION(NAME,MAIL,MOBILE,ADDRESS)
# WRITE A ANOTHER CLASS NAMED AS STAFF WITH STAFF INFORMATION FUNCTION WITH ARGUMENT OF (NAME,MAIL,MOBILE,ADDRESS,DEPT)
# WRITE A ANOTHER CLASS NAMED AS STUDENT WITH STUDENT INFORMATION FUNCTION WITH ARGUMENT OF NAME,MAIL,MOBILE,ADDRESS,DEPT
# INHERIT STUDENT WITH SCHOOL AND STAFF WITH SCHOOL
# ASK WHETHER STUDENT OR STAFF TO USER AND CALL THE FUNCTION ACCORDING TO THE USER

class School:
    def __init__(self,Name,Mail,Mobile,Address):
        self.Name = Name
        self.Mail = Mail
        self.Mobile = Mobile
        self.Address = Address
    def School_Details(self):
        print("My Names Is: ",self.Name,"\nMy Mail_Id Is: ",self.Mail,"\nMy Mobile_No Is: ",self.Mobile,"\nMy Address Is: ",self.Address)
class Staff(School):
    def __init__(self,Name,Mail,Mobile,Address,Department):
        super().__init__(Name,Mail,Mobile,Address)
        self.Department = Department
    def Staff_Details(self):
        super().School_Details()
        print("My Department Is: ",self.Department)
class Student(School):
    def __init__(self,Name,Mail,Mobile,Address,Department):
        super().__init__(Name,Mail,Mobile,Address)
        self.Department = Department
    def Student_Details(self):
        super().School_Details()
        print("My Department Is: ",self.Department)
User = input("Enter Student Or Staff: ").strip().lower()

if User == "student":
    Obj_Student = Student("Ashif","mohammedashif605@gmail.com",9385642379,"Madurai","Bsc Computer Science")
    Obj_Student.Student_Details()
else:
    Obj_Staff = Staff("Leo","nanthandaleo605@gmail.com",7010045018,"Kashmir","Bsc Information Technology")
    Obj_Staff.Staff_Details()
