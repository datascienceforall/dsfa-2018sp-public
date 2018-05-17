# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """Your answer is not the correct length."""
msg2 = """The final item in difference_from_expected is off"""
msg3 = """Your answer should be an array"""


#end err msg definition
def check6_3(difference_from_expected):
	if type(difference_from_expected) != np.ndarray:
		print(msg3)
	elif difference_from_expected.size !=272:
		print(msg1)
	elif difference_from_expected.item(271)!=2964: 
		print(msg2)
	else:
		print("Your answer looks ok. It's either correct or close.")
