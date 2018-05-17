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


def check5_5(proportion_in_20th_century,proportion_in_21st_century):
	correctanswer1 = 0.684
	correctanswer2 = 0.316
	if isinstance(proportion_in_20th_century,type(correctanswer1)) and isinstance(proportion_in_21st_century,type(correctanswer2)):
		if (proportion_in_20th_century ==correctanswer1) and (proportion_in_21st_century == correctanswer2):
			print(correct_msg)
		else:
			print(default_err_msg)
	else:
		print(type_err_msg)
