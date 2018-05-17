# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """You need to replace the ... in the definition of characters_q1
with 1, 2, 3, 4, or 5."""
msg2 = """Your answer should be 1, 2, 3, 4, or 5."""
#end err msg definition
def check2_1(characters_q1):
    if not characters_q1 != ... : 
        print(msg1)
    elif not 1 <= characters_q1 <= 5 : 
        print(msg2)
    else: 
        print("Your solution looks ok!")
