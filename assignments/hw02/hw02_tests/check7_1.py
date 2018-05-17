from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """Your answer is not correct."""

#end err msg definition

#'''
#correcttable = Table().with_columns(
#    'fruit name', make_array(4, 3, 3),
#    'count', make_array('apple', 'orange', 'pineapple'))
#'''

def check7_1(fruits):
	if type(fruits) != tables.Table:
		print(msg1)        
	elif fruits.sort(1).column(1).item(2) == 'pineapple':
		print(msg1)
	else:
		print("Your answer looks ok!")
