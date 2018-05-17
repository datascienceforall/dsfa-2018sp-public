#begin import modules
import numpy as np
import math
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """ It looks like you're not making an array.  You shouldn't need to
 use .item anywhere in your solution."""
msg2 = """ You made an array, but it doesn't have the right numbers in it."""
default_err_msg = """Something is wrong with your solution, but it's not
one of the common mistakes we expected.  See if you can figure
out what the mistake might be, or ask a neighbor or TA for help!"""
#end err msg definition
def check4_3_1(population,population_magnitudes):
    if not type(population_magnitudes) == np.ndarray : 
        print(msg1)
    elif not sum(abs(population_magnitudes - np.log10(population))) < 1e-6 : 
        print(msg2)
    else: 
        print("Your solution looks ok!")
