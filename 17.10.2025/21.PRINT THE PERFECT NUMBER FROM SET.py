# PRINT THE PERFECT NUMBER FROM SET.

Numbers = {6,12,28,24,30}
for i in Numbers:
    Sum = 0
    for j in range(1,i):
        if i%j == 0:
            Sum+=j
    if Sum == i:
        print(i,"Is A Perfect Number")
    else:
        print(i,"Is Not Perfect Number")
    
    
