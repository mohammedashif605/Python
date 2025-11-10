# Reverse Print - Print all list items in reverse order using a loop (no-built-in reverse
n = [10,20,30,40,50]
m = len(n)
o = []
for i in range(m-1,-1,-1):
    o+=(n[i], )
print(o)
