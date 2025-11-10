# CREATE DICTIONARY.

def Get_Dict():
    d = {}
    n = int(input("Enter The Range : "))
    for i in range(n):
        Key = int(input("Enter The Key : "))
        Value = int(input("Enter The Value : "))
        d[Key] = Value
    return d
        

def Print_Dict_Value(d):

    for i in d.items():
        Values = d.values()
    print("The Dictionary Values Are :\n",Values)
    return d
        


def Sum_Dict_Value(d):
    print("Sum Of Dictionary Value Is :",sum(d.values()))
