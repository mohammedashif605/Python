# PYTHON FUNCTION TO SUM ALL THE NUMBERS IN A LIST USING ARBITRARY ARGUMENT.

def Sum(*a):
    sum=0
    for i in a:
        sum+=i
    print("The Sum Of All Number Is : ",sum)
Sum(1,2,3,4,5,6)
