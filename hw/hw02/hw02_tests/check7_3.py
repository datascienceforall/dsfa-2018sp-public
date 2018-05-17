from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """Please type 'Yes' or 'No'."""
msg2 = """Your answer is not correct."""



#end err msg definition
def check7_3(all_different):
	if type(all_different) != str:
		print(msg1)
		return
	all_different = all_different.lower()
	if all_different not in ["yes","no"]:
		print(msg1)
	elif all_different != "no":
		print(msg2)
	else:
		print("Your answer looks ok!")