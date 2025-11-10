# PROGRAM TO CHECK WHETHER A NUMBER IS A PALINDROME OR NOT.

Number = input("Enter The Number : ")
Number1 = Number[::-1]
if Number == Number1:
    print("It Is Palindrome")
else:
    print("It Is Not Palindrome")
