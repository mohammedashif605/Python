# Find those numbers that are divisible by 7 and multiple of 5, between  1 and 100.

print("Numbers Divisible By Both 7 and 5 : ")
for  i in range (1,101):
    if i % 7 == 0 and i % 5 == 0:
        print(i)
            
