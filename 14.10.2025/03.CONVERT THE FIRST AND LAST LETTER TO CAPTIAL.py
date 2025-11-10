# Convert the first and last letter to captial.

n = input()
m = n[0].upper() + n[1:-1] + n[-1].upper()
print(m)
