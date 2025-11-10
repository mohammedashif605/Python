# Remove a specific item from a list entered by the user.

list = ["1","2","3","4","5"]
user = input("Enter The Number (1/2/3/4/5): ")
if user in list:
    list.remove(user)
    print("The Updated Number List Is : ",list)
else:
    print("Please Enter The Number In List")
