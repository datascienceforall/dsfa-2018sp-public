# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """It looks like you didn't give anything the name
seconds_in_a_decade.  Maybe there's a typo, or maybe you
just need to run the cell below Question 3.2 where you defined
seconds_in_a_decade.  (Click that cell and then click the "run
cell" button in the menu bar above.)"""
msg2 = """It looks like you didn't change the cell to define
seconds_in_a_decade appropriately.  It should be a number,
computed using Python's arithmetic.  For example, this is
almost right:
  seconds_in_a_decade = 10*365*24*60*60"""
msg3 = """It looks like you didn't account for leap years.
There were 2 leap years and 8 non-leap years in this period.
Leap years have 366 days instead of 365."""
msg4 = """Something is wrong with your solution, but it's not
one of the common mistakes we expected.  See if you can figure
out what the mistake might be, or ask a neighbor or TA for help!
"""
#end err msg definition
def check3_2(seconds_in_a_decade):
	if 'seconds_in_a_decade' not in vars():
		print(msg1)
	elif seconds_in_a_decade == ...:
		print(msg2)
	elif seconds_in_a_decade == 315360000:
		print(msg3)
	elif seconds_in_a_decade != 315532800:
		print(msg4)
	else:
		print("Your solution passes the checks!")
