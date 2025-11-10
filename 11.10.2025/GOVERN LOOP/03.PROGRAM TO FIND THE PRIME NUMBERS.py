# PROGRAM TO FIND THE PRIME NUMBERS.

Number = int(input("Enter The Number : "))
count=0
if Number <= 1:
    print(Number,"Is Not Prime Number")
else:
    for i in range(2,Number):
        if Number%i == 0:
            count+=1
if count==0:
    print(Number,"Is Prime Number")
else:
    print(Number,"Is Not Prime Number")
