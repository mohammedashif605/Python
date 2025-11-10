# Square Each number - create a list [1,2,3,4,5] and print each number's square using a loop.

n = []
for i in range (1,6):
 n.append(i)
print(n)
for i in n:
    s = i**2
    print("The Square Value Of",i,"Is",s)
