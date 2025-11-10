exp = int (input("Enter Your Experience : "))
if exp < 5:
    print("Sorry You Are Not Eligible For Bonus")
    salary = int (input("Enter Your Salary : "))
    print("Your Salary Is : ",salary)
else:
    print("You Are Eligible For Bonus")
    salary = int (input("Enter Your Salary : "))
    sal_bon = salary * (5/100)
    final_bonus = salary + sal_bon
    print("Your Salary With Bonus : ",final_bonus)
    
    
