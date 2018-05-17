# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """At least one of your answers is incorrect."""

def check4_1(first_product,second_product,third_product,fourth_product):
    if first_product != 6594:
        print(msg1)
    elif second_product != 663168:
    	print(msg1)
    elif third_product != 6660320568:
    	print(msg1)
    elif fourth_product != -39250:
    	print(msg1)
    else: 
        print("All of your answers are correct!")