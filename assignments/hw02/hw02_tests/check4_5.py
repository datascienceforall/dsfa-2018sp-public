# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """Your answer is incorrect"""

def check4_5(celsius_temperature_ranges):
    if type(celsius_temperature_ranges) != np.ndarray:
        print(msg1)
    elif len(celsius_temperature_ranges) != 65000:
        print(msg1)
    elif round(sum(celsius_temperature_ranges)) != 768351.0:
        print(msg1)
    elif celsius_temperature_ranges.item(1) != 10.0:
        print(msg1)
    else: 
        print("Correct!")
