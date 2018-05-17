#begin import modules
import math
from datascience import *
import numpy as np
# end import modules

#begin msg definitions
default_err_msg = "Something is wrong with your solution.  See if you can figure out what the mistake might be, or ask a neighbor or TA for help!"
type_err_msg = "Your solution is not in the correct format!"
correct_msg = "Your solution is correct!"
okay_msg = "The format of your solution looks okay!"
#end msg definitions


def check6_4(average_latitude,average_longitude):
	correctanswer1 = 39.186464523495417
	correctanswer2 = -90.992580812926292
	if isinstance(average_latitude,type(correctanswer1)) and isinstance(average_longitude,type(correctanswer2)):
		if (average_latitude ==correctanswer1) and (average_longitude == correctanswer2):
			print(correct_msg)
		else:
			print(default_err_msg)
	else:
		print(type_err_msg)
