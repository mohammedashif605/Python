# WRITE A PROGRAM CREATE CLASS INDIA,USA,UK
# DESCRIBE THE COUNTRY NAME IN CONSTRUCTOR
# DESCRIBE THE CAPITAL IN CAPITAL FUNCTION
# DESCRIBE THE LANGUAGE IN LANGUAGE FUNCTION

class India:
    def __init__(self):
        self.Country = "India"
    def Capital(self):
        print("The Capital Of",self.Country,"Is New Delhi")
    def Language(self):
        print("The National Language Of",self.Country,"Is Hindi")
class USA:
    def __init__(self):
        self.Country = "USA"
    def Capital(self):
        print("The Capital Of",self.Country,"Is Washington")
    def Language(self):
        print("The National Language Of",self.Country,"Is English")
class UK:
    def __init__(self):
        self.Country = "UK"
    def Capital(self):
        print("The Capital Of",self.Country,"Is London")
    def Language(self):
        print("The National Language Of",self.Country,"Is English")
Obj_India = India()
Obj_USA = USA()
Obj_UK = UK()
for Country in (Obj_India,Obj_USA,Obj_UK):
    Country.Capital()
    Country.Language()
    print()
