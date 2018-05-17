#begin import modules
import numpy as np
import math
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
default_err_msg = """Something is wrong with your solution, but it's not
one of the common mistakes we expected.  See if you can figure
out what the mistake might be, or ask a neighbor or TA for help!"""
#end err msg definition
def check4_1_3(hello_world_components):
    if not type(hello_world_components) == np.ndarray : 
        print(default_err_msg)
    elif not len(hello_world_components) == 5 : 
        print(default_err_msg)
    elif not all(hello_world_components == np.array(["Hello", ",", " ", "world", "!"])) : 
        print(default_err_msg)
    else: 
        print("Your solution looks ok!")
