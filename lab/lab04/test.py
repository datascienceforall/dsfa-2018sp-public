import math
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

def is_string_type(x):
    return x in (str, np.str_)

def is_close(a,b):
    return np.isclose(a, b, rtol=1e-09)

def fails_generic(mode):
    if mode == CHECK:
        fails("Incorrect. Something is wrong with your answer, but it's not a mistake we were expecting.  Check with a TA or neighbor to see what might be wrong.", mode)
    elif mode == TEST:
        fails("Incorrect.", mode)
    else:
        assert "Illegal mode"

def correct(mode):
    passes('Correct.', mode)
    
def check_bool_ask_if_err(b, mode):
    if b:
        correct(mode)
    else:
        fails_generic(mode)

def check_fruitful_function(fn, arg, mode):
    if not callable(fn):
        fails("Incorrect. Make sure you've used the right syntax to define the function.", mode)
        return False
    elif fn(arg) == None:
        fails("Incorrect. Make sure you used the return keyword in your function.", mode)    
        return False
    else:
        return True        
        
###############################################################################################
    
def check1_1(total_pay_type, mode=CHECK):
    if total_pay_type == tables.Table:
        fails('Incorrect. Make sure you are examining the type of the values in the column, not the table.', mode)
    elif total_pay_type == np.ndarray:
        fails('Incorrect. Make sure you are examining the type of the values in the column, not the column itself.', mode)
    elif total_pay_type == '$53.25 ':
        fails('Incorrect. Make sure you are examining the type of the value, not the value itself.', mode)        
    else:
        check_bool_ask_if_err(is_string_type(total_pay_type), mode) 
        
def check1_2(mark_hurd_pay_string, mode=CHECK):
    check_bool(mark_hurd_pay_string == '$53.25 ', mode)

def check1_3(mark_hurd_pay, mode=CHECK):
    if type(mark_hurd_pay) == str:
        fails('Incorrect. Your answer should be a number, not a string.', mode)
    elif not is_number(mark_hurd_pay):
        fails('Incorrect. Your answer should be a number.', mode)
    elif is_close(mark_hurd_pay, 53.25):
        fails('Incorrect. Make sure your answer is in dollars, not millions of dollars.', mode)
    else:
        check_bool_ask_if_err(is_close(mark_hurd_pay, 53250000.0), mode)

def check1_4(convert_pay_string_to_number, mode=CHECK):
    test1 = convert_pay_string_to_number('$100')
    if not is_number(test1):
        fails('Incorrect. Make sure your function returns a number.', mode)
    elif is_close(test1, 53250000.0):
        fails('Incorrect. Make sure your function uses pay_string, not mark_hurd_pay_string.', mode)
    else:
        test2 = convert_pay_string_to_number('$3.14')
        check_bool(is_number(test2) and is_close(test1, 100000000.0) and is_close(test2, 3140000.0), mode)
    
def check2_1(to_percentage, mode=CHECK):
    if not check_fruitful_function(to_percentage, .1, mode):
        pass
    elif not is_number(to_percentage(.1)):
        fails("Incorrect. Make sure your function returns a number.", mode)
    elif is_close(to_percentage(.1), .1):
        fails("Incorrect. Make sure your function multiplies by 100.", mode)
    elif is_close(to_percentage(.1), 20.0):
        fails("Incorrect. Make sure your function uses the proportion argument to compute the return value.", mode)
    else:
        check_bool_ask_if_err(is_close(to_percentage(.1), 10.0), mode)
    
def check2_2(a_percentage, mode=CHECK):
    check_bool(is_number(a_percentage) and is_close(round(a_percentage,1), 70.7), mode)
    
def check2_3(disemvowel, mode=CHECK):
    if not check_fruitful_function(disemvowel, '', mode):
        pass
    elif disemvowel('a') == 'a':
        fails("Incorrect. Maybe you returned the original string, not the result of a call to replace?", mode)
    else:
        check_bool_ask_if_err(disemvowel('abcdefghijklmnopqrstuvwxyz') == 'bcdfghjklmnpqrstvwxyz', mode)
    
def check2_4(num_non_vowels, mode=CHECK):
    if not check_fruitful_function(num_non_vowels, '', mode):
        pass
    elif num_non_vowels('a') == 1:
        fails("Incorrect. Maybe you forgot to remove the vowels?", mode)
    else:
        check_bool_ask_if_err(num_non_vowels('abcdefghijklmnopqrstuvwxyz') == 21, mode)
    
def check2_5(highest_ranking_year, mode=CHECK):
    if not check_fruitful_function(highest_ranking_year, 1, mode):
        pass
    elif highest_ranking_year(4) == 2015:
        fails("Incorrect. Maybe your function ignores the rank argument?", mode)
    else:
        check_bool_ask_if_err(highest_ranking_year(9) == 2008, mode)
    
def check3_1(some_functions, mode=CHECK):
    if not is_np_array(some_functions):
        fails('Incorrect. Make sure you created an array.', mode)
    elif len(some_functions) != 3:
        fails('Incorrect. Make sure your array has three elements.', mode)
    elif not all([callable(f) for f in some_functions]):
        fails('Incorrect. At least one of your array elements is not a function.', mode)
    else:
        correct(mode)
    
def check3_2(compensation, mode=CHECK):
    if not is_table(compensation):
        fails('Incorrect. The result should be a table.', mode)
    elif 'Total Pay ($)' not in compensation.labels:
        fails("Incorrect. The 'Total Pay ($)' column is missing from your table.", mode)
    elif not is_number(compensation.column('Total Pay ($)').item(0)):
        fails("Incorrect. Make sure the column contains numbers.", mode)        
    else:
        check_bool_ask_if_err(
            is_close(compensation.column('Total Pay ($)')[0:3], 
                     [53250000., 53240000., 44910000.]).all(), 
            mode)
    
def check3_3(average_total_pay, mode=CHECK):
    if not is_number(average_total_pay):
        fails('Incorrect. The answer should be a number.', mode)
    else:
        check_bool_ask_if_err(is_close(round(average_total_pay,2), 11445294.11), mode)
    
def check3_4(cash_proportion, mode=CHECK):
    if not is_np_array(cash_proportion):
        fails('Incorrect. Your answer should be an array.', mode)
    else:
        with np.errstate(invalid='ignore'):
            check_bool_ask_if_err(is_close(cash_proportion[0:3], 
                                           [0.01784038, 0.01784373, 0.55421955]
                                           ).all(), mode)
    
def check3_5(with_previous_compensation, mode=CHECK):
    labels = {'% Change', 'Cash Pay', 'Company (Headquarters)', 'Equity Pay', 'Name', \
              'Other Pay', 'Rank', 'Ratio of CEO pay to average industry worker pay', \
              'Total Pay', 'Total Pay ($)'}
    if not is_table(with_previous_compensation):
        fails('Incorrect. Make sure your answer is a table.', mode)
    elif not (labels <= set(with_previous_compensation.labels)):
        fails('Incorrect. Your table is missing some columns from the original table.', mode)
    elif '2014 Total Pay ($)' not in with_previous_compensation.labels:
        fails('Incorrect. Your table is missing the 2014 Total Pay ($) column.')
    elif "(No previous year)" in with_previous_compensation.column("% Change"):
        fails('Incorrect. Make sure to remove the CEOs who did not receive compensation in the previous year.', mode)
    elif with_previous_compensation.num_rows != 81:
        fails('Incorrect. Your table does not have the right number of rows.', mode)
    else:
        pays = np.around(with_previous_compensation.sort('2014 Total Pay ($)', descending=True).column('2014 Total Pay ($)')[0:3],2)
        check_bool_ask_if_err(is_close(pays, [67700000.  , 46298969.07, 42329411.76]).all(), mode)
    
def check3_6(average_pay_2014, mode=CHECK):
    if not is_number(average_pay_2014):
        fails('Incorrect. The answer should be a number.', mode)
    else:
        check_bool_ask_if_err(is_close(round(average_pay_2014,2), 11649176.12), mode)
    
def check4_1(estimate_ceos30, mode=CHECK):
    if not is_number(estimate_ceos30):
        fails('Incorrect. Your answer should be a number.', mode)
    elif .02*102 <= estimate_ceos30 <= .08*102:
        passes('Ok! That looks like a reasonable visual estimate.', mode)
    else:
        fails("That estimate looks off. Try again.", mode)

def check4_2(num_ceos30, mode=CHECK):
    check_bool_ask_if_err(num_ceos30 == 5, mode)
    
    