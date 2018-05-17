# begin import modules
from datascience import *
import numpy as np
from numbers import Number
# end import modules
#begin err msg definition
msg1 = """Incorrect. Hint: the shortest is a number between 40 and 50."""
msg2 = """Incorrect. Hint: the longest is a number between 70 and 130."""
msg3 = """Incorrect. Hint: the average is between the shortest and the longest."""


#end err msg definition
def check6_1(shortest,longest,average):
	if not (isinstance(shortest,Number) and 40 <= shortest <= 50):
		print(msg1)
	elif not (isinstance(longest,Number) and 70 <= longest <= 130): 
		print(msg2)
	elif not (isinstance(average,Number) and shortest <= average <= longest):
		print(msg3)
	else:
		print("Your answer looks ok. It's either correct or close.")

