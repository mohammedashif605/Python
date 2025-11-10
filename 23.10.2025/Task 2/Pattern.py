# CREATE PATTERN.PY

def Rightangle(n):

    for i in range (0,n):
        for j in range (0,i+1):
            print("*",end="")
        print()
    return n


def Leftangle(n):

    for i in range (0,n):
        for j in range (1,n-i):
            print(" ",end="")
        for k in range (0,i+1):
            print("*",end="")
        print()
    return n


def Inverseright(n):

    for i in range (n,0,-1):
        for j in range (1,i+1):
            print("*",end="")
        print()
    return n 

def Inverseleft(n):

    for i in range (n,0,-1):
        for j in range (0,n-i):
            print(" ",end="")
        for k in range (1,i+1):
            print("*",end="")
        print()
    return n
            
