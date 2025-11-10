# CREATE LOGICAL.PY FILE

def Prime(a):
    count=0
    if a <= 1:
        print(a,"Is Not Prime Number")
    else:
        for i in range(2,a):
            if a%i == 0:
                count+=1
        if count==0:
            print(a,"Is Prime Number")
        else:
            print(a,"Is Not Prime Number")
        return a

def Perfect(a):
    sum = 0
    for i in range(1,a):
        if a%i == 0:
            sum+=i
    if a == sum:
        print(a,"Is Perfect Number")
    else:
        print(a,"Is Not Perfect Number")
    return a

def Armstrong(a):
    s = 0
    temp = a
    d = len(str(a))
    while a>0:
        r = a%10
        s+=r**d
        a//=10
    if s == temp:
        print(s,"It Is Armstrong Number")
    else:
        print(s,"It Is Not Armstrong Number")
    return s
