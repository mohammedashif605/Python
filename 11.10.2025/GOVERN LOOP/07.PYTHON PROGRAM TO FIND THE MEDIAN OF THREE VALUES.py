# PYTHON PROGRAM TO FIND THE MEDIAN OF THREE VALUES.

A = float(input("Enter The First Number : "))
B = float(input("Enter The Second Number : "))
C = float(input("Enter The Third Number : "))
if B<=A<=C or C<=A<=B:
    Median = A
elif A<=B<=C or C<=B<=A:
    Median = B
else:
    Median = C
print("The Median Is : ",Median)
