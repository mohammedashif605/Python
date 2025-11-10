# FIND THE NUMBER OF PRIME NUMBERS IN A SET.

Set = {0,1,3,5,7,8,10,21,36}
for i in Set:
    Element=i
    count=0
    if Element <= 1:
        print(Element,"Is Not Prime Number")
    else:
         for i in range(2,Element):
            if Element%i == 0:
                count+=1
         if count==0:
            print(Element,"Is Prime Number")
                
