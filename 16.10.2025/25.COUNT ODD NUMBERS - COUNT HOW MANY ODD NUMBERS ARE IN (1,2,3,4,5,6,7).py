# COUNT ODD NUMBERS - COUNT HOW MANY ODD NUMBERS ARE IN (1,2,3,4,5,6,7).

Tuple = (1,2,3,4,5,6,7)
count = 0
for i in Tuple:
    if i%2!=0:
        count+=1
print("The Count Of Odd Number Is : ",count)
