# FIND THE KEY FOUND IN DICTIONARY USING ARBITRARY KEYWORD ARGUMENT.

def dictionary(**a):
    for i in a.keys():
        print("Key Is",i)
dictionary(1=2,2=3,3=4,4=5)
    
