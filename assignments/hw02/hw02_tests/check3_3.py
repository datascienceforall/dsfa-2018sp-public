# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """Your solution is incorrect."""

def check3_3(index_of_last_element):
    if index_of_last_element != 141: 
        print(msg1)
    else: 
        print("Correct!")
