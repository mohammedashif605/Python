# MULTIPLY ALL THE ITEMS IN A DICTIONARY.

Dictionary = {1:10,2:10,3:10,2:3,7:10,2:4}
print(Dictionary)
Mul_Key = 1
Mul_Values = 1
for i in Dictionary.keys():
    Mul_Key*=i
for j in Dictionary.values():
    Mul_Values*=j
print("The Multiply Of Key Is : ",Mul_Key)
print("The Multiplay Of Value Is : ",Mul_Values)
    
