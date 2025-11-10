# FIND THE NUMBER OF EVEN NUMBERS AND ODD NUMBERS IN A SET

Numbers = {1,2,3,4,5,6,7,8,9,10,11}
Even_Count = 0
Odd_Count = 0
for i in Numbers:
    if i%2==0:
        Even_Count+=1
    else:
        Odd_Count+=1
print("The Number Of Odd Numbers Is : ",Odd_Count)
print("The Numbers Of Even Numbers Is : ",Even_Count)
