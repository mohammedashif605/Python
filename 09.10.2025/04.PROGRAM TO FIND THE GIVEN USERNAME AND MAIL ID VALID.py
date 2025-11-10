user = str (input("Enter The User Name : "))
if user == "Ashif":
    print("Username Is Verified")
    mail = str (input("Please Enter Email ID : "))
    if mail == "mohammedashif605@gmail.com":
        print("Login Successfully")
    else:
        print("Please Enter Valid Email ID")
else:
    print("Please Enter Valid User Name")
