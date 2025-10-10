# Display n terms of natural number and their sum

n = int(input("Enter The N Terms : "))
if n > 0:
    sum = 0
    for i in range (1,n+1):
        print(i)
        sum+=i
    print("Sum of Natural Numbers Is : ",sum)
else:
    print("Please Enter Valid Number")
