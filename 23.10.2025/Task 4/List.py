def Get_List():
    List = []
    Num = int(input("Enter The Number Of Elements : "))
    for i in range(Num):
        Element = int(input("Enter Element : "))
        List.append(Element)
    return List
    

def Print_List_Values(List):
    print("The List You Entered:", List)
    return List

def Odd_Even(List):
    Odd = []
    Even = []
    for i in List:
        if i % 2 == 0:
            Even.append(i)
        else:
            Odd.append(i)
    return Odd, Even
