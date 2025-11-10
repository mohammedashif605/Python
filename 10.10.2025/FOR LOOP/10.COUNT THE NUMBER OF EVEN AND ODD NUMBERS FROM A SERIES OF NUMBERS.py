# Count the number of even and odd numbers from a series of numbers.

n =  int(input("Enter The N Value : "))
odd = 0
even = 0
for i in range (1,n+1):
    if i % 2 == 0:
        even+=1
    else:
        odd+=1
print("Total Odd Number Is : ",odd)
print("Total Even Number Is : ",even)
