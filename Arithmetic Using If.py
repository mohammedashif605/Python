a = int(input("Enter The A Value : "))
b = int(input("Enter The B Value : "))
typ = str(input("Enter The Type Addition/Subtraction/Multiplication/Division : "))
if typ == "Addition":
    print("The Addition Value Is : ",a+b)
elif typ == "Subtraction":
    print("The Subtraction Value Is :",a-b)
elif typ == "Multiplication":
    print("The Mulplication Value Is :",a*b)
elif typ == "Division":
    print("The Division Value Is :",a/b)
else:
    print("Enter Valid Command")
