# PYTHON FUNCTION TO PRINT THE EVEN NUMBERS FROM A GIVEN LIST USING ARBITRARY ARGUMENT.

def Even(*a):
    even=()
    for i in a:
        if i%2 == 0:
            even+=(i,)
    print("The Even Numbers Are : ",even)
Even(1,2,3,4,5,6,7,8,9,10)
