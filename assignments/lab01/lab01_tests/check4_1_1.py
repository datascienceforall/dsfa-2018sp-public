# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """# Fill in the line
#   num_avenues_away = ...
# in the cell above."""
msg2 = """# Remember to compute the absolute value of 7-10.  Traveling
# "-3 blocks" doesn't really make sense!"""
msg3 = """Something is wrong with your solution, but it's not
one of the common mistakes we expected.  See if you can figure
out what the mistake might be, or ask a neighbor or TA for help!
"""
#end err msg definition
def check4_1_1(num_avenues_away,manhattan_distance):
	if num_avenues_away == ...:
		print(msg1)
	elif num_avenues_away == -3:
		print(msg2)
	elif num_avenues_away != 3 or manhattan_distance != 1462:
		print(msg3)
	else:
		print("Your solution passes the checks!")
