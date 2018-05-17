import math
from datascience import *
import numpy as np
# end import modules



#begin  msg definitions
default_err_msg = "Something is wrong with your solution.  See if you can figure out what the mistake might be, or ask a neighbor or TA for help!"
type_err_msg = "Your solution is not in the correct format!"
correct_msg = "Your solution is correct!"
okay_msg = "The format of your solution looks okay!"
#end msg definitions

#end err msg definition

def check3_1(my_flower):
	if isinstance(my_flower,list):
		if not((type(my_flower[0]) == int) and (type(my_flower[1]) == str) and (len(my_flower[1])>0)):
			print(default_err_msg)
		else:
			print(correct_msg)
	else:
		print(type_err_msg)

