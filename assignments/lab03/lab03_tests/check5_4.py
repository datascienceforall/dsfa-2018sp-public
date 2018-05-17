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


def check5_4(average_20th_century_rating,average_21st_century_rating):
	correctanswer1 = 8.2783625730994146
	correctanswer2 = 8.2379746835443033
	if isinstance(average_20th_century_rating,type(correctanswer1)) and isinstance(average_21st_century_rating,type(correctanswer2)):
		if (abs(average_20th_century_rating - correctanswer1) < 1e-5) and (abs(average_21st_century_rating - correctanswer2) < 1e-5):
			print(correct_msg)
		else:
			print(default_err_msg)
	else:
		print(type_err_msg)

