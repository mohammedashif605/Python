# WRITE A PYTHON PROGRAM TO GET DAYS BETWEEN TWO DATES.
# SAMPLE DATES : 2000,2,28, 2001,2,28
# EXPECTED OUTPUT : 366 DAYS, 0:00:00

import datetime

a = datetime.datetime(2000,2,28)
b = datetime.datetime(2001,2,28)
c = b - a
print("The Difference Between Two Dates Is : ",c)
