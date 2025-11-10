# WRITE A PYTHON PROGRAM TO CALCULATE AN AGE IN YEARS.

from datetime import datetime

x = datetime.today()
Birthday = datetime(2002,4,26)
Age = x-Birthday
print(Age)

