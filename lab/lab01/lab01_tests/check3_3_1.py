# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """Fill in the line
  time = ...
with something like:
  time = 4.567
(except with the correct number)."""
msg2 = """Read the text above the question to see what
time should be."""
msg3 = """Fill in the line
  estimated_distance_m = ...
with something like:
  estimated_distance_m = 4.567
(except with the correct number)."""
msg4 = """Note that the units are meters, but the text used
centimeters."""
msg5 = """Read the text above the question to see what
estimated_distance_m should be."""
#end err msg definition
def check3_3_1(time,estimated_distance_m):
	if time == ...:
		print(msg1)
	elif round(time, 5) != 1.2:
		print(msg2)
	elif estimated_distance_m == ...:
		print(msg3)
	elif estimated_distance_m == 113:
		print(msg4)
	elif round(estimated_distance_m, 5) != 1.13:
		print(msg5)
	else:
		print("Your solution passes the checks!")
