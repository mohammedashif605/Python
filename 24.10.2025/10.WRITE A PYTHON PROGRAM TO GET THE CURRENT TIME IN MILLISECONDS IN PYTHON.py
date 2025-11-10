# WRITE A PYTHON PROGRAM TO GET THE CURRENT TIME IN MILLISECONDS IN PYTHON.

from datetime import datetime

x = datetime.now()
milliseconds = int(x.timestamp() * 1000)
print(milliseconds)
