# PROGRAM TO CHECK IF A SET IS A SUBSET OF ANOTHER SET.

Set1 = {1,2,3,4,5,6,7}
Set2 = {1,2,3,4,5,6,7,8,9,10,11,12}
if Set1.issubset(Set2):
    print(Set1,"Is Subset Of",Set2)
else:
    print(Set1,"Isn't Subset Of ",Set2)
