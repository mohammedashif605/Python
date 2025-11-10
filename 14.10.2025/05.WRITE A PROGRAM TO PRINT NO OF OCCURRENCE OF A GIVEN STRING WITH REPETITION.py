# Write a program to print no of occurrence of a given string with repetition.
# Text = "I am New to this office but not New to Role"

Text = "I am New to this office but not New to Role"
n = Text.lower().split()
print(n)
for i in set(n):
    print(i,"=",n.count(i))
