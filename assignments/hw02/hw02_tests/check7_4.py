from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """Your answer is not correct."""

#end err msg definition

#correcttable = Table().with_columns(
#    'box ID', make_array(25274,26187,43566,48800,52357,53686,57181,57930),
#    'fruit name',make_array('apple','strawberry','peach','orange','strawberry','kiwi','strawberry','grape'),
#    'count sold', make_array(0,25,17,35,102,3,101,355),
#    'price per fruit ($)',make_array(0.8,0.15,0.8,0.6,0.25,0.5,0.2,0.06))

def check7_4(sales):
	if type(sales) != tables.Table:
		print(msg1)
	elif sales.sort(3).column(3).item(7) != 0.8:
		print(msg1)
	else:
		print("Your answer looks ok!")
