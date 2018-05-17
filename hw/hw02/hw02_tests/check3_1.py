# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """You need to replace the ... in the definition of weird_numbers with an array."""
#msg2 = """Your answer is not the right data type."""
msg3 = """It looks like you wrote:
          'some_numbers.item(3)'
          But the third element has index 2, not 3."""
msg4 = """Your answer isn't quite correct."""
#end err msg definition
def check3_1(third_element):
    if not third_element != ... : 
        print(msg1)
    #elif type(third_element) != np.int32:
    #	print(msg2)
    elif third_element == -10: 
        print(msg3)
    elif third_element != -6: 
        print(msg4)
    else: 
        print("Your solution looks ok!")
