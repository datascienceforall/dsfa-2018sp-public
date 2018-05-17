from datascience import *
import numpy as np
from numbers import Number
# end import modules
#begin err msg definition
msg1 = """Your answer is pretty far off."""
msg2 = """Your answer should be a number."""

#end err msg definition
def check6_4(average_from_error):
	if not isinstance(average_from_error, Number):
		print(msg2)
	elif not 15 < average_from_error < 25:
		print(msg1)
	else:
		print("Your answer looks ok. It's either correct or close.")
