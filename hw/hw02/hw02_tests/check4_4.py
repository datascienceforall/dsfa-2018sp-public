# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """It looks like you multiplied and subtracted in the wrong order."""
msg2 = """Your answer is incorrect"""

def check4_4(celsius_max_temperatures):
    if type(celsius_max_temperatures) != np.ndarray:
        print(msg2)
    elif sum(celsius_max_temperatures) == 356705.0:
        print(msg1)
    elif len(celsius_max_temperatures) != 65000:
        print(msg2)
    elif sum(celsius_max_temperatures) != 1280677.0:
        print(msg2)
    elif celsius_max_temperatures.item(2003) != 20.0:
        print(msg2)
    else: 
        print("Correct!")
