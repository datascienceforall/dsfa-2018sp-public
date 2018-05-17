# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """You need to replace the ... in the definition of characters_q2
with 1, 2, or 3."""
msg2 = """Your answer should be 1, 2, or 3."""
#end err msg definition
def check2_2(characters_q2):
    if not characters_q2 != ... : 
        print(msg1)
    elif not 1 <= characters_q2 <= 3 : 
        print(msg2)
    else: 
        print("Your solution looks ok!")
