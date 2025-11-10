# PYTHON FUNCTION THAT COUNT NUMBER OF VOWELS, CONSONANT AND SPECIAL CHARACTER
# IN A PASSED STRING

def VCS(a):
    Vowels="AEIOURaeiou"
    Vowels_Count = 0
    Consonant_Count = 0
    Special_Count = 0
    for Word in a:
        if Word.isalpha():
            if Word in Vowels:
                Vowels_Count+=1
            else:
                Consonant_Count+=1
        elif not Word.isalnum() or Word.isspace():
            Special_Count+=1
    print("Vowels : ",Vowels_Count)
    print("Consonants : ",Consonant_Count)
    print("Special Characters :",Special_Count)
a=input("Enter The String : ")
VCS(a)
