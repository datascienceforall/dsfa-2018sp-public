# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
#end err msg definition
def check5_1(botan_distance_from_average_m):
	if round(botan_distance_from_average_m, 5) != 0.162:
		print('Double check your solution: something is wrong.')
	else:
		print("Your solution passes the checks!")
