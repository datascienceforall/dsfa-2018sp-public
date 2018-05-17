# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """# Read the text above the question to see what
# estimated_distance_m should be."""
msg2 = """# Compute predicted_distance_m using the formula in the text
# above.  Hint: it should start with something like this:
#   predicted_distance_m = (1/2) * gravity_constant ..."""
#end err msg definition
def check4_2_1(estimated_distance_m,predicted_distance_m,difference):
    assert round(estimated_distance_m, 5) == 1.13, msg1
    assert round(predicted_distance_m, 5) == 1.17022, msg2
    assert round(difference, 5) == 0.04022
    print("Your solution passes the tests")
