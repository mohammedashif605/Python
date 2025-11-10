print ("                            LOGICAL OPERATORS")

print("1. AND OPERATOR")

a1 = input("Enter The First Boolean Value : ")
b1 = input("Enter The Second Boolean Value : ")
c1 = a1=='TRUE'
d1 = b1=='TRUE'
print("The Result Is : ",c1 and d1)

print("2. OR OPERATOR")

a2 = input("Enter The First Boolean Value : ")
b2 = input("Enter The Second Boolean Value : ")
c2 = a2=='TRUE'
d2 = b2=='TRUE'
print("The Result Is : ",c2 or d2)

print("3. NOT OPERATOR")

a3 = input("Enter The Boolean Value : ")
b3 = a3=='TRUE'
print("The Result Is : ",not b3)

print("4. AND & OR OPERATORS")

a4 = input("Enter The First Boolean Value : ")
b4 = input("Enter The Second Boolean Value : ")
c4 = input("Enter The Third Boolean Value : ")
d4 = a4=='TRUE'
e4 = b4=='TRUE'
f4 = c4=='TRUE'
print("The Result Is : ",(d4 and e4) or f4 )

print("5. NOT & AND OPERATOR")

a5 = input("Enter The First Boolean Value : ")
b5 = input("Enter The Second Boolean Value : ")
c5 = a5=='TRUE'
d5 = b5=='TRUE'
print("The Result Is : ",(not c5) and d5 )
