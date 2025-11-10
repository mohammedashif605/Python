# PROGRAM TO FIND COMMON ELEMENTS IN THREE LISTS USING SETS.

List1 = [1,2,3,4,5,6]
List2 = [1,3,5,7]
List3 = [1,6,7,8]
List4 = set(List1).intersection(set(List2),set(List3))
print(List4)
