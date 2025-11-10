# WRITE A PYTHON CLASS NAMED AS PERSONAL WITH INFORMATION FUNCTION WITH ARGUMENT OF NAME,EMAIL,MOBILE,ADDRESS
# WRITE A ANOTHER CLASS NAMED AS EDUCATIONAL WITH INFORMATION FUNCTION WITH ARGUMENT OF MARKS OF EACH SUBJECT, TOTAL AND PERCENTAGE
# WRITE A ANOTHER CLASS NAMED AS BANK WITH INFORMATION FUNCTION WITH ARGUMENT OF ACC_NO,BRANCH_NAME,BANK_NAME,IFSC_CODE,AVAILABLE BAL
# INHERIT BANK WITH EDUCTIONAL AND EDUCATIONAL WITH PERSONAL

class Person:
    def __init__(self,Name,Email,Mobile,Address):
        self.Name = Name
        self.Email = Email
        self.Mobile = Mobile
        self.Address = Address
    def Details(self):
        print("My Name Is: ",self.Name,"\nMy Email Is: ",self.Email,"\nMy Mobile_No Is: ",self.Mobile,"\nMy Address Is: ",self.Mobile)
class Education(Person):
    def __init__(self,Name,Email,Mobile,Address,Marks,Total,Percentage):
        super().__init__(Name,Email,Mobile,Address)
        self.Marks = Marks
        self.Total = Total
        self.Percentage = Percentage
    def Information(self):
        super().Details()
        print("My Mark Is: ",self.Marks,"\nMy Total Is: ",self.Total,"\nMy Percentage Is: ",self.Percentage)
class Bank(Education):
    def __init__(self,Name,Email,Mobile,Address,Marks,Total,Percentage,Account_No,Bank_Name,Branch_Name,Ifsc,Availble_Bal):
        super().__init__(Name,Email,Mobile,Address,Marks,Total,Percentage)
        self.Account = Account_No
        self.Bank = Bank_Name
        self.Branch = Branch_Name
        self.Ifsc = Ifsc
        self.Balance = Availble_Bal
    def Final(self):
        super().Information()
        print("My Account Number Is: ",self.Account,"\nMy Bank Name Is: ",self.Bank,"\nMy Branch Name Is: ",self.Branch,"\nMy Ifsc Code Is: ",self.Ifsc,"\nMy Balance Is: ",self.Balance)
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
Obj_All = Bank("Ashif","mohammedashif605@gmail.com",9385642379,"Madurai",Marks,Total,Percentage,741441454,"SBI","ARASARADI","SBIN014525",9.20)
Obj_All.Final()
        
    

    
    
    
