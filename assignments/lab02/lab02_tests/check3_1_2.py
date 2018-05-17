#begin import modules
import IPython.display
import math
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """ It looks like you didn't load an image.  Hint:
 your code should start like this:
   art = IPython.display.Image(..."""
msg2 = """ It looks like you loaded the wrong image."""
default_err_msg = """Something is wrong with your solution, but it's not
one of the common mistakes we expected.  See if you can figure
out what the mistake might be, or ask a neighbor or TA for help!"""
#end err msg definition
def check3_1_2(art):
    if not type(art) == IPython.core.display.Image : 
        print(msg1)
    elif not 'The_Death_of_Socrates' in art.url : 
        print(msg2)
    else: 
        print("Your solution looks ok!")
