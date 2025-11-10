# How to count vowels in a string.

n = input("Enter The Word : ")
m = n.lower()
vowels = "aeiou"
count = 0
for i in m:
    if i in vowels:
        count+=1
print("The Number Of Vowles Is : ",count)
