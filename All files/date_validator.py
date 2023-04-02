
# Python3 code to demonstrate working of
# Validate String date format
# Using strptime()
from datetime import datetime

# initializing string
test_str = '3/50/1995'

# printing original string
print("The original string is : " + str(test_str))

# initializing format
format = "%d/%m/%Y"

# checking if format matches the date
res = True

# using try-except to check for truth value
try:
	res = bool(datetime.strptime(test_str, format))
except ValueError:
	res = False

# printing result
print("Does date match format? : " + str(res))
