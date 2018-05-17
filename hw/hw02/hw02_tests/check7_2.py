from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """Your answer is not correct."""



#end err msg definition
def check7_2(inventory):
	if type(inventory) != tables.Table or inventory.sort(0).column(0).item(0) !=25274:
		print(msg1)
	else:
		print("Your answer looks ok!")

