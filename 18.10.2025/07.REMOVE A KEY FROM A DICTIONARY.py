# REMOVE A KEY FROM A DICTIONARY.

Dictionary = {1:"Ashif",2:"Cricket",3:"Kabbadi"}
print("Before Remove :",Dictionary)
Key = int(input("Enter The Key (1/2/3) : "))
Dictionary.pop(Key)
print("After Remove : ",Dictionary)
