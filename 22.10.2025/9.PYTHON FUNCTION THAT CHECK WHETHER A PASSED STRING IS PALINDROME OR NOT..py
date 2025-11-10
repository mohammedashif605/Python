# PYTHON FUNCTION THAT CHECK WHETHER A PASSED STRING IS PALINDROME OR NOT.

def Palindrome(a):
    Reverse=""
    for i in a:
        Reverse = i+Reverse
    if Reverse == a:
        print(a,"Is A Palindrome")
    else:
        print(a,"It Is Not A Palindrome")
a = input("Enter The String :").lower()
        
Palindrome(a)
