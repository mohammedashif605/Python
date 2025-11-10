# WRITE A PYTHON PROGRAM TO CONVERT A STRING TO DATETIME.
        # SAMPLE STRING : JULY 1 14 2:43PM
        # EXPECTED OUTPUT : 2014-07-01 14:43:00

from datetime import datetime

x = "July 1 14 2:43pm"
y = datetime.strptime(x, "%B %d %y %I:%M%p")
print(y)
