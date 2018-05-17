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
def check4_1_1_2(collection_times):
    if not type(collection_times) == np.ndarray : 
        print(default_err_msg)
    elif not len(collection_times) == 744 : 
        print(default_err_msg)
    elif not all(collection_times == np.arange(0, 31*24*60*60, 60*60)) : 
        print(default_err_msg)
    else: 
        print("Your solution looks ok!")
