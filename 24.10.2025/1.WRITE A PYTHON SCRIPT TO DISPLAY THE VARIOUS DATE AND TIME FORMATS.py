# WRITE A PYTHON SCRIPT TO DISPLAY THE VARIOUS DATE AND TIME FORMATS.

# Current Date And Time:
import datetime as d
x =d.datetime.now()
print("The Current Date Time Is : ",x)
# Current Year:
print("The Current Year Is : ",x.year)
# Month Of Year:
print("The Current Month Is : ",x.month)
# Week Number Of Year:
print("The Current Week Number Of The Year Is : ",x.strftime("%U"))
# Week Day Of The Week:
print("The Weekday Of The Week Is : ",x.strftime("%w"))
# Day Of Year:
print("The Day Of Year Is : ",x.strftime("%j"))
# Day Of The Month:
y =x.timetuple()
print("The Day Of The Month Is : ",y[2])
# Day Of Week:
print("The Day Of The Week Is : ",y[6])

