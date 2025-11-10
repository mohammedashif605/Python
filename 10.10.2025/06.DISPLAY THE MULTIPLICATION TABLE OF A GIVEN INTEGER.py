# Display the multiplication table of a given interger.

n = int(input("Enter The Table Value : "))
print(n,"Table Is : \n")
for i in range (1,11):
    table = i*n
    print(i,"x",n," =",table)
