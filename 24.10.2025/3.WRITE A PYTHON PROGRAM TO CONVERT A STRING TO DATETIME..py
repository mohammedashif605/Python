# WRITE A PYTHON PROGRAM TO CONVERT A STRING TO DATETIME.

from datetime import datetime
a = "26-04-2002"
b = datetime.strptime(a, "%d-%m-%Y")
print(b)

from datetime import datetime
a = "2002-04-26"
b = datetime.strptime(a, "%Y-%m-%d")
print(b)

from datetime import datetime
a = "April 26,2002"
b = datetime.strptime(a, "%B %d,%Y")
print(b)
