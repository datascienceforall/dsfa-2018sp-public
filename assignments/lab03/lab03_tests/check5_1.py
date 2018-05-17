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


def check5_1(average_rating_in_forties):
	correctanswer = 8.2571428571428562
	if isinstance(average_rating_in_forties,type(correctanswer)):
		if abs(average_rating_in_forties - 8.2571428571428562) < 1e-5:
			print(correct_msg)
		else:
			print(default_err_msg)
	else:
		print(type_err_msg)
