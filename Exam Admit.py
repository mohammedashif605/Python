no_of_class = int (input("Total Number Of Classes Held Is : "))
attend_class = int (input("Total Number Of Classes You Attended : "))
percentage = (attend_class/no_of_class) * 100
print("Your Percentage Of Attendence Is : ",percentage)
if percentage >= 75:
    print("You Allowed To Sit In Exam ")
else :
    print("You Are Not Allowed To Sit In Exam ")
