# FIND THE NUMBER NAMES CONTAINS WITH "Ku"

Names = {"Kumbakonam","Vilaku","Ashif","Kumbam","Nishok"}
New_Names = set()
for i in Names:
    New_Names.add(i.lower())
print(New_Names)
Word = "ku"
count = 0
for i in New_Names:
    if Word in i:
        count+=1
print("The Count of Ku Is : ",count)

    







