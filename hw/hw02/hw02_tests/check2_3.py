# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1a = """You need to replace the ... in with_commas with your answer."""
msg1b = """You need to replace the ... in without_commas with your answer.""" 
msg2a = """Your answer to with_commas should be a string."""
msg2b = """Your answer to without_commas should be a string."""
msg3a = """Your answer to with_commas is the right data type, but not correct."""
msg3b = """Your answer to without_commas is the right data type, but not correct."""
#end err msg definition
def check2_3(with_commas,without_commas):
    if with_commas == ... : 
        print(msg1a)
    elif type(with_commas) != str:
    	print(msg2a)
    elif with_commas !='Eats, Shoots, and Leaves':
    	print(msg3a)
    else: 
        print("with_commas looks ok!")
    if not without_commas != ... : 
        print(msg1b)
    elif type(without_commas) != str:
    	print(msg2b)
    elif without_commas !='Eats Shoots and Leaves':
    	print(msg3b)
    else: 
        print("without_commas looks ok!")
