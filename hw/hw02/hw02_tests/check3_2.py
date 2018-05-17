# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """There is an error with your solution."""

some_numbers = make_array(-1, -3, -6, -10, -15)
elements_of_some_numbers2 = Table().with_columns(
    "English name for position", make_array("first", "second", "third", "fourth", "fifth"),
    "Index",                     make_array("0", "1", "2", "3", "4"),
    "Element",                   some_numbers)

def check3_2(elements_of_some_numbers):
	#if elements_of_some_numbers.all() != CorrectTable.all(): 
    if (elements_of_some_numbers["English name for position"] == elements_of_some_numbers2["English name for position"]).all() and (elements_of_some_numbers["Index"] ==   elements_of_some_numbers2["Index"]).all() and (elements_of_some_numbers["Element"] == elements_of_some_numbers2["Element"]).all():
        print("Your solution looks ok!")
    else:
        print(msg1)
