# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """The value you assign to names_q1 should be 1, 2, 3, or 4."""
msg2 = """The value you assign to names_q2 should be 1, 2, 3, or 4."""
#end err msg definition
def check3(names_q1,names_q2):
    if not 1 <= names_q1 <= 4 :
        print(msg1)
    elif not 1 <= names_q2 <= 4 :
        print('msg2')
    else:
        print("Your solution looks ok!")
