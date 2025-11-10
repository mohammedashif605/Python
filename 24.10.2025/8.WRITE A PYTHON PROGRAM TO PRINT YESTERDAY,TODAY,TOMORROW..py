# WRITE A PYTHON PROGRAM TO PRINT YESTERDAY,TODAY,TOMORROW.

from datetime import datetime,timedelta

x = datetime.today()
y = x-timedelta(days=1)
z = x+timedelta(days=1)
print("The Current Day Is ",x)
print("The Yesterday Is ",y)
print("The Tommorow Is ",z)
