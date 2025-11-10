# WRITE A PYTHON PROGRAM TO SUBTRACT FIVE DAYS FROM THE CURRENT DATE.
# CURRENT DATE = 2015-06-22

from datetime import datetime,timedelta
x = datetime(2015,6,22)
y = x -timedelta(days=5)
print("Current Date Is : ",x)
print("Date After Subtracting 5 Days Is ",y)
