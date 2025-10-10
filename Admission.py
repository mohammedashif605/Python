apt = int (input("Enter Your Aptitude Mark : "))
gd = int (input("Enter Your Group Discussion Mark : "))
tech = int (input("Enter Your Technical Mark : "))
hr = int (input("Enter Your HR Mark : "))
total = apt + gd + tech + hr
print("Your Total Mark Is : ",total)
if apt >= 85 and gd >= 90 and tech >=80 and hr >=95:
    if total >= 390 and total <=400:
        print("You Are Eligible and Your Salary Is : 30000")
    elif total >= 380 and total < 390:
        print("You Are Eligible and Your Salary Is : 28000")
    elif total >= 370 and total < 380:
        print("You Are Eligible and Your Salary Is : 25000")
    elif total >= 350 and total < 370:
        print("You Are Eligible and Your Salary Is : 20000")
else:
    print("You Are Not Eligible")
