# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """You need to replace the ... in the definition of surivor_answer 
with 1, 2, or 3."""
msg2 = """Your answer should be 1, 2, or 3."""
#end err msg definition
def check1_1(surivor_answer):
    if not surivor_answer != ... : 
        print(msg1)
    elif not 1 <= surivor_answer  <= 3: 
        print(msg2)
    else: 
        print("Your solution looks ok!")