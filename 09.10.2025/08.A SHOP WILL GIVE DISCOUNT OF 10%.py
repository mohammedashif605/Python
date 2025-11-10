pur_amount = int (input("Enter Your Purchase Cost  : "))
if pur_amount > 1000:
    print("Congratulations You Are Eligible for 10% Discount")
    discount = pur_amount * (10/100)
    finalcost = pur_amount - discount
    print("After The Discount Your Purchase Cost Is : ",finalcost)
else:
    print("You Total  Cost Is : ",pur_amount)
