import numpy as np
from datascience import *

from numbers import Number
from enum import Enum

Modes = Enum('Modes', 'CHECK TEST')
CHECK = Modes.CHECK
TEST = Modes.TEST

def result(passes, msg, mode):
    if mode==TEST:
        assert passes, msg
    elif mode==CHECK:
        print(msg)
    else:
        assert "Illegal mode"
        
def passes(msg, mode):
    result(True, msg, mode)
    
def fails(msg, mode):
    result(False, msg, mode)
    
def check_bool(correct, mode):
    if correct:
        passes('Correct.', mode)
    else:
        fails('Incorrect.', mode)
        
def check_multiple_choice_in_bounds(ans, outof, mode):
    if not (isinstance(ans, int) and 1 <= ans <= outof):
        fails('Incorrect.  Answer must be an integer between 1 and {}.'.format(str(outof)), mode)
    else:
        passes('Ok.', mode)
        
def is_table(t):
    return type(t) == tables.Table

def eq_table(t1, t2):
    if not(is_table(t1) and is_table(t2)):
        return False
    if not len(t1.keys()) == len(t2.keys()):
        return False
    for k in t1.keys():
        if not k in t2.keys():
            return False
        if not np.array_equal(t1[k], t2[k]):
            return False
    return True

def is_number(x):
    return isinstance(x, Number)

def is_np_array(x):
    return type(x) == np.ndarray

def check1_1(dissimilarity, mode=CHECK):
    correct = is_number(dissimilarity) and round(dissimilarity) == 14061.0
    check_bool(correct, mode)

def check1_2(data_types, mode=CHECK):
    check_multiple_choice_in_bounds(data_types, 3, mode)
    
def check1_3(why_abs_value, mode=CHECK):
    check_multiple_choice_in_bounds(why_abs_value, 4, mode)
    
def check1_4(revised_dissimilarity, mode=CHECK):
    correct = is_number(revised_dissimilarity) and round(revised_dissimilarity) == 506.0
    check_bool(correct, mode)
    
def check2_1(unemployment, mode=CHECK):
    t = Table().read_table("unemployment.csv")
    check_bool(eq_table(unemployment, t), mode)

def check2_2(by_nei, by_nei_pter, mode=CHECK):
    t = Table().read_table("unemployment.csv")
    check_bool(eq_table(by_nei, t.sort('NEI', descending=True)), mode)
    check_bool(eq_table(by_nei_pter, t.sort('NEI-PTER', descending=True)), mode)

def check2_3(greatest_nei, mode=CHECK):
    t = Table().read_table("unemployment.csv")
    check_bool(eq_table(greatest_nei, t.sort('NEI', descending=True).take(np.arange(10))), mode)

def check2_4(pter, mode=CHECK):
    if not is_np_array(pter):
        fails('Incorrect. The answer should be an array.', mode)
    elif (pter.max() < 0.0):
        fails('Incorrect. You might have subtracted in the wrong order.', mode)
    else:
        t = Table.read_table("unemployment.csv")
        check_bool(np.allclose(pter, t["NEI-PTER"] - t["NEI"]), mode)
    
def check2_5(by_pter, mode=CHECK):
    if not is_table(by_pter):
        fails('Incorrect. The answer should be a table.', mode)
    elif not ('PTER' in by_pter.labels):
        fails('Incorrect. Your table does not include a column named PTER.', mode)
    elif not np.isclose(round(by_pter.column('PTER').item(0), 4), 1.9315):
        fails('Incorrect. It looks like you forgot to sort in descending order.', mode)
    else:
        t = Table.read_table("unemployment.csv")
        pter = (t["NEI-PTER"] - t["NEI"])
        pter_sorted = t.with_column('PTER', pter).sort('PTER', descending=True).column('PTER')
        check_bool(np.allclose(by_pter.column('PTER'), pter_sorted), mode)
    
def check3_1(us_birth_rate, mode=CHECK):
    if not (is_number(us_birth_rate) and 0 < us_birth_rate < 1):
        fails('Incorrect. The answer should be a number between 0 and 1.', mode)
    else:
        passes('Ok.', mode)

def check3_2(fastest_growth, mode=CHECK):
    if not is_np_array(fastest_growth):
        fails('Incorrect. The answer should be an array.', mode)
    elif len(fastest_growth) != 5:
        fails('Incorrect. There should be five states in the array.', mode)
    elif fastest_growth.item(0) != 'Utah':
        fails('Incorrect. You might be computing the growth rate incorrectly.', mode)
    else:
        passes('Ok.', mode)
   
def check3_3(movers, mode=CHECK):
    if not (is_number(movers) and 0 <= movers <= 52):
        fails('Incorrect. The answer should be a number between 0 and 52.', mode)
    elif movers in [8, 52]:
        fails('Incorrect. Double check how you compute the migration rate.', mode)
    elif movers in [0, 38, 51]:
        fails('Incorrect. Double check how you choose which rows to count.', mode)
    else:
        passes('Ok.', mode)
        
def check3_4(ne_births, mode=CHECK):
    if not is_number(ne_births):
        fails('Incorrect. The answer should be a number.', mode)
    elif ne_births == 0:
        fails('Incorrect. Did you notice that the values in the REGION column are strings?', mode)
    else:
        passes('Ok.', mode)
    
def check3_5(less_than_ne_births, mode=CHECK):
    if not (is_number(less_than_ne_births) and 0 <= less_than_ne_births <= 52):
        fails('Incorrect. The answer should be a number between 0 and 52.', mode)
    else:
        passes('Ok.', mode)
    
    