# begin import modules
from datascience import *
import numpy as np
from numbers import Number
# end import modules
#begin err msg definition
msg1 = """Incorrect. Hint: the biggest decrease is at least 30 but not 47."""



#end err msg definition
def check6_2(biggest_decrease):
	if not(isinstance(biggest_decrease,Number)) or biggest_decrease < 30 or biggest_decrease == 47:
		print(msg1)
	else:
		print("Your answer looks ok. It's either correct or close.")

