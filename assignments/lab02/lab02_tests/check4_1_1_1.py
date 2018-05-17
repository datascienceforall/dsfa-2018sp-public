#begin import modules
import math
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
default_err_msg = """Something is wrong with your solution, but it's not
one of the common mistakes we expected.  See if you can figure
out what the mistake might be, or ask a neighbor or TA for help!"""
#end err msg definition
def check4_1_1_1(multiples_of_99):
    if not type(multiples_of_99) == np.ndarray : 
        print(default_err_msg)
    elif not len(multiples_of_99) == 102 : 
        print(default_err_msg)
    elif not all(multiples_of_99 == np.arange(0, 9999+99, 99)) : 
        print(default_err_msg)
    else: 
        print("Your solution looks ok!")
