# WRITE A PYTHON PROGRAM TO ADD 5 SECONDS TO THE CURRENT TIME.

from datetime import datetime,timedelta

x = datetime.now()
y = x+timedelta(seconds=5)
print("The Current Time Is : ",x)
print("The Current Time After 5 Seconds Is : ",y)
