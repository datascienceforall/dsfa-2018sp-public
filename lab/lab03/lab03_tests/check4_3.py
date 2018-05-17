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


def check4_3(earliest_movie_title):
	correctanswer = 'The Kid'
	if isinstance(earliest_movie_title,type(correctanswer)):
		if earliest_movie_title == correctanswer:
			print(correct_msg)
		else:
			print(default_err_msg)
	else:
		print(type_err_msg)
