    # PYTHON FUNCTION TO PRINT A SIMPLE CALCULATOR.

def Add(a,b):
    c = a+b
    print("Addition Value Is ",c)
    return c

def Sub(a,b):
    c = a-b
    print("Subtraction Value Is ",c)
    return c

def Mul(a,b):
    c = a*b
    print("Multiplication Value Is ",c)
    return c

def Div(a,b):
    c = a/b
    print("Division Value Is ",c)
    return c

a = int(input("Enter The A Value : "))
b = int(input("Enter The B Value : "))
x = Add(a,b)
y = Sub(a,b)
z = Mul(x,y)
Div(z,x)
