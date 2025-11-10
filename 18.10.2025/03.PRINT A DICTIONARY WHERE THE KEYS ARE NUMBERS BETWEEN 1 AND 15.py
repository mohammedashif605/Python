# PRINT A DICTIONARY WHERE THE KEYS ARE NUMBERS BETWEEN 1 AND 15 (BOTH INCLUDED)
# THE VALUES ARE SQUARE OF KEYS

Dictionary = {}
Pairs = int(input("Enter The Number Of Pairs : "))
for i in range(Pairs):
    Key = int(input("Enter The Key : "))
    Value = Key**2
    Dictionary[Key]=Value
print("Dictionary Elements : ",Dictionary)
    
    
