# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """Fill in the line that currently says
  predicted_distance_m = ...
in the cell above."""
msg2 = """Compute predicted_distance_m using the formula in the text
above.  Hint: it should start with something like this:
  predicted_distance_m = (1/2) * gravity_constant ..."""
msg3 = """Something is wrong with your solution, but it's not
one of the common mistakes we expected.  See if you can figure
out what the mistake might be, or ask a neighbor or TA for help!
""" 
#end err msg definition
def check3_3_2(difference,predicted_distance_m):
	if predicted_distance_m == ...:
		print(msg1)
	elif round(predicted_distance_m, 5) != 1.17022:
		print(msg2)
	elif round(difference, 5) != 0.04022:
		print(msg3)
	else:
		print("Your solution passes the checks!")
