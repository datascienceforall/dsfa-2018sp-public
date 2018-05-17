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
def check2_3_1(sentence_length):
    if not sentence_length == 896 : 
        print(default_err_msg)
    else: 
        print("Your solution looks ok!")
