# REMOVE A LAST KEY FROM A DICTIONARY USING ARBITRARY KEYWORD ARGUMENT.

def Dictionary(**a):
        a.popitem()
        print(a)
Dictionary(a=15,b="Ashif",c=18.5,d=12)
