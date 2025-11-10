# COUNT VOWELS - CREATE A TUPLE OF LETTERS AND COUNT HOW MANY VOWELS ARE THERE USING A LOOP.


Tuple  = ('A','b','e','c','I','i','o','d')
Vowels = ('a','e','i','o','u')
count = 0
for i in Tuple:
    if i.lower() in Vowels:
        count+=1
print("The Count Of Vowels Is : ",count)
