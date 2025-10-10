# Program to calculate the factorial of given number

n = int(input("Enter The N Value  : "))
fact = 1
if n < 0:
    print("There is No Factorial Number For A Negative Number ")
else:
    for i in range (1,n+1):
        fact*=i
    print("Factorial Number Is :",fact)
    
    
