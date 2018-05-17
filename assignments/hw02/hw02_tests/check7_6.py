from datascience import *
import numpy as np
from numbers import Number
# end import modules
#begin err msg definition
msg1 = """Your answer is not correct.
If you're stuck, here's a hint: You want to multiply the count
sold in each box by the per-item price of fruits in that box.
You can use elementwise multiplication for that.
Then you want the sum of those products.  Use sum()."""


#end err msg definition
def check7_6(total_revenue):
	if not (isinstance(total_revenue,Number) and 106.84 < total_revenue < 106.86):
		print(msg1)
	else:
		print("Your answer looks ok!")
