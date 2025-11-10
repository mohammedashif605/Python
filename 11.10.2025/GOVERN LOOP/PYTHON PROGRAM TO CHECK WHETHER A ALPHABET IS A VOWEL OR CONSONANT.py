# PYTHON PROGRAM TO CHECK WHETHER A ALPHABET IS A VOWEL OR CONSONANT.

Alpha = input("Enter A Single Alphabet : ").lower()
if len(Alpha) == 1 and Alpha.isalpha():
    if Alpha in "aeiou":
        print(Alpha,"Is a Vowel")
    else:
        print(Alpha,"Is a Consonant")
else:
    print("Please Enter Single Alphabet")
