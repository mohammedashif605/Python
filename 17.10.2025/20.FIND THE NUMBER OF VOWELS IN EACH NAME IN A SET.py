# FIND THE NUMBER OF VOWELS IN EACH NAME IN A SET.

Names = {"Ashif","Nishok","Amirthavarshan"}
New_Names = set()
for i in Names:
    New_Names.add(i.lower())
print(New_Names)
Vowels = "aeiou"
for i in New_Names:
    count =  0
    for j in i:
        if j in Vowels:
            count+=1
    print(i,"=",count,"Vowels")







