# CHECK WHETHER A GIVEN KEY ALREADY EXISTS IN A DICTIONARY.

Dictionary = {1:2,2:3,3:4,4:5}
Key  = int(input("Enter The Key : "))
if Key in Dictionary:
    print("Key Is Exist")
else:
    print("Key Is Not Exist")
