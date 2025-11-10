temp = int (input("Enter The Temperature : "))
if temp<0:
    print("Freezing Weather")
elif temp<=10:
    print("Very Cold Weather")
elif temp<=20:
    print("Cold Weather")
elif temp<=30:
    print("Normal In Temp")
elif temp<=40:
    print("Its Hot")
else:
    print("Very Hot")
