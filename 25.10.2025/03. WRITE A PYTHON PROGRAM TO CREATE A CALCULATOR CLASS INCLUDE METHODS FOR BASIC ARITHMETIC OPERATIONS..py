# WRITE A PYTHON PROGRAM TO CREATE A CALCULATOR CLASS INCLUDE METHODS FOR BASIC ARITHMETIC OPERATIONS.

class Calculator:
    def Addition(self,a,b):
        return a+b
    def Subtraction(self,a,b):
        return a-b
    def Multiplication(self,a,b):
        return a*b
    def Division(self,a,b):
        return a/b
Obj_Calculator = Calculator()
a = int(input("Enter The A Value : "))
b = int(input("Enter The B Value : "))
print("Addition Value Is : ",Obj_Calculator.Addition(a,b))
print("Subtraction Value Is : ",Obj_Calculator.Subtraction(a,b))
print("Multiplication Value Is : ",Obj_Calculator.Multiplication(a,b))
print("Division Value Is : ",Obj_Calculator.Division(a,b))
