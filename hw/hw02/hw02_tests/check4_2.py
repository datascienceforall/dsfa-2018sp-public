# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """Your answer must be an array"""
msg2 = """Your answer is incorrect"""

def check4_2(products):
    if type(products) != np.ndarray:
        print(msg1)
    elif not np.allclose(products, np.array([6594, 663168, 6660320568, -39250])):
        print(msg2)
    else: 
        print("Correct!")