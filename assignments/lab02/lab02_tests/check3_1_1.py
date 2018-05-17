#begin import modules
import math
import math
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """ Hint: You can write the sine of 1.5*pi as:
   math.sin(1.5 * math.pi)"""
default_err_msg = """Something is wrong with your solution, but it's not
one of the common mistakes we expected.  See if you can figure
out what the mistake might be, or ask a neighbor or TA for help!"""
#end err msg definition
def check3_1_1(sine_of_pi_over_four):
    if not round(sine_of_pi_over_four, 8) == 0.70710678 : 
        print(msg1)
    else: 
        print("Your solution looks ok!")
