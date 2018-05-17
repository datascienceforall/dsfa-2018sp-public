# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
#end err msg definition
def check5_1_1(min_height_difference):
	if round(min_height_difference, 5) != 0.05:
		print('Double check your solution: something is wrong.')
	else:
		print("Your solution passes the checks!")
