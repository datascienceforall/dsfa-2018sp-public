# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """The value you assigned to dissimilarity was not numeric---that is, it
was not either a int or a float.  Try assigning a numeric value to dissimilarity,
such as 42 or 3.14.
"""
#end err msg definition
def check5_1(dissimilarity):
    if not isinstance(dissimilarity, (int, float)) :
        print(msg1)
    else:
        print("Your solution looks ok!")
