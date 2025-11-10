# Add names entered by the user into a list until they type 'stop'

n = []
while True:
    list = input("Enter the names (type 'stop' to end) : ")
    if list.lower() == "stop":
        break
    n.append(list)
print("The Names Are : ",n)
