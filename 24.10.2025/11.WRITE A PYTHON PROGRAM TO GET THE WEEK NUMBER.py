# WRITE A PYTHON PROGRAM TO GET THE WEEK NUMBER.
# SAMPLE DATE : 2015,6,16
# EXPECTED OUTPUT : 25

from datetime import datetime

x = datetime(2015,6,16)
print(x.strftime("%V"))
