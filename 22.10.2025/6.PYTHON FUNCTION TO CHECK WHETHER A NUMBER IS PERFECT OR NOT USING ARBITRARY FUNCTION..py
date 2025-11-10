# PYTHON FUNCTION TO CHECK WHETHER A NUMBER IS PERFECT OR NOT USING ARBITRARY FUNCTION.

def Perfect(*a):
    for i in a:
        sum=0
        for j in range(1,i):
            if i%j==0:
                sum+=j
        if i == sum :
            print(i,"Is Perfect Number")
        else:
            print(i,"Is Not Perfect Number")
Perfect(6,28,124,156)
