#begin import modules
import math
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """ Hint 1: Try to make the word "bookkeeper"!

 Hint 2: After writing this:
   you = 'keep'
 the value of the variable named 'the' will be
   'beekeeper'"""
default_err_msg = """Something is wrong with your solution, but it's not
one of the common mistakes we expected.  See if you can figure
out what the mistake might be, or ask a neighbor or TA for help!"""
#end err msg definition
def check2_1_1(you,this):
    if not 'beeper'.replace('p', you).replace('bee', this)[::-1] == 'repeekkoob' : 
        print(msg1)
    else: 
        print("Your solution looks ok!")
