# FIND SMALLEST NUMBER - FIND THE SMALLEST VALUE IN (45,12,89,33,67) USING A LOOP.

Tuple = (45,12,89,33,67)
Small = Tuple[1]
for i in Tuple:
    if i<Small:
        Small = i
print("The Smallest Value Is : ",Small)
