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


def check4_2(imdb_by_year):
	correctanswer = ['The Kid', 'The Gold Rush', 'The General']
	if isinstance(imdb_by_year,Table):
		if list(imdb_by_year.column('Title').take(range(3))) == correctanswer:
			print(correct_msg)
		else:
			print(default_err_msg)
	else:
		print(type_err_msg)
