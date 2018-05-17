# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """Your answer is incorrect"""

def check4_3(fixed_products):
    if not (type(fixed_products) == np.ndarray and np.allclose(fixed_products, np.array([66234, 6661248, 66900162648, -394250]))):
        print(msg1)
    else: 
        print("Correct!")