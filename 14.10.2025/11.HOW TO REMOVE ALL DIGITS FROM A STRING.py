# How to remove all digits from a string.

string = input("Enter The String : ")
remove = ""
for i in string:
    if not i.isdigit():
        remove+=i
print(remove)
