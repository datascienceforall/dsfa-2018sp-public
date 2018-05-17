from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """ It looks like your table doesn't have all 3 columns that are in the inventory table."""
msg2 = """It looks like you forgot to subtract off the sales."""
msg3 = """Your answer is not correct."""


#end err msg definition
def check7_7(remaining_inventory):
	if type(remaining_inventory) != tables.Table:
		print(msg3)    
	elif remaining_inventory.num_columns != 3:
		print(msg1)
	elif remaining_inventory.sort(0).column(2).item(5) ==45:
		print(msg2)
	elif remaining_inventory.sort(0).column(2).item(7) !=162:
		print(msg3)
	else:
		print("Your answer looks ok!")


