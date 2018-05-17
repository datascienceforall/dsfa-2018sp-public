# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
#msg1 = """You need to replace the ... in the definition of weird_numbers with your answer."""
msg2 = """Your answer needs to be an array."""
msg3 = """Your answer is the correct data type, an array, but isn't correct."""
#end err msg definition
correctarray = np.array([-2,np.math.sin(1.2),3,5**np.math.cos(1.2)]) 
def check2_1(weird_numbers):
	#print(type(weird_numbers))
	the_type = type(weird_numbers)
	if the_type != np.ndarray:
		print(msg2)
	elif not np.allclose(correctarray,weird_numbers): 
	    print(msg3)
	else: 
	    print("Your solution looks ok!")
