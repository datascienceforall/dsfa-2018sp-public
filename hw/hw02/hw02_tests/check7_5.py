from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """Your answer is not correct."""


#end err msg definition
def check7_5(total_fruits_sold):
	if total_fruits_sold != 638:
		print(msg1)
	else:
		print("Your answer looks ok!")
