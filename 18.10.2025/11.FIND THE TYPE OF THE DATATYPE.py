# FIND THE TYPE OF DATA TYPE:

Dictionary = {3:2.5,"Name":1,(1,2,3):[1,2,3],3.13:{1,23,4},True:False}
for key,value in Dictionary.items():
    print(f"Key : {key} == Type : {type(key)}")
    print(f"Value : {value} == Type : {type(value)}\n")
