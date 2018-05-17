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
    if not isinstance(ans, int):
        fails('Incorrect. Answer should be an integer.', mode)
    elif not 1 <= ans <= outof:
        fails('Answer must be an integer between 1 and {}.'.format(str(outof)), mode)
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

def is_iterable(obj):
    try:
        _ = iter(obj)
        return True
    except TypeError:
        return False

def fails_generic(mode):
    if mode == CHECK:
        fails("Incorrect. Something is wrong with your answer, but it's not a mistake we were expecting.  Check with a TA or neighbor to see what might be wrong.", mode)
    elif mode == TEST:
        fails("Incorrect.", mode)
    else:
        assert "Illegal mode"

def correct(mode):
    passes('Correct.', mode)
    
def ok(mode):
    passes('Ok.', mode)
    
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
        
def check_table_labels(table, labels, mode):
    if not is_table(table):
        fails('Incorrect. Your answer should be a table.', mode)
        return False
    elif table.labels != labels:
        fails('Incorrect. Double check your column labels and order.', mode) 
        return False
    else:
        return True

def check_select_all_that_apply(lst, max_val, mode):
    if not (is_iterable(lst) and all(is_number(x) and x in range(1, max_val+1) for x in lst)):
        fails('Your answer is not in the form of a list of numbers between 1 and {}. Try again.'.format(str(max_val)), mode)
    else:
        ok(mode)

def check_table_labels_sorted(table, labels_sorted, mode):
    if not is_table(table):
        fails('Incorrect. Your answer should be a table.', mode)
        return False
    elif tuple(sorted(table.labels)) != labels_sorted:
        fails('Incorrect. Double check your column labels.', mode)
        return False
    else:
        return True
    
def check_all_choices_in_bounds(ans, outof, mode):
    if not (isinstance(ans, list) and np.all([1 <= i <= outof for i in ans])):
        fails('Incorrect.  Answer must be integers between 1 and {}.'.format(str(outof)), mode)
    else:
        passes('Ok.', mode)
###############################################################################################

def check1_1(p_winning_after_two_flips, mode=CHECK):
    if not is_number(p_winning_after_two_flips): 
        fails("Your answer is not a number.", mode)
    elif p_winning_after_two_flips > 1:
        fails("Probability cannot be greater than 1", mode)
    else:
        ok(mode)
        
def check1_3(reasonable_test_statistics, mode=CHECK):
    def has_duplicate(l):
        out = [i for i in l if l.count(i) > 1]
        return not len(out) == 0
    if not isinstance(reasonable_test_statistics, list):
        fails("Your answer should be a list.", mode)
    elif has_duplicate(reasonable_test_statistics):
        fails("Your answer should not have duplicates", mode)
    else:
        check_all_choices_in_bounds(reasonable_test_statistics, 6, mode)
        
def check1_4(simulate, mode=CHECK):
    result = simulate()
    if not is_number(result):
        fails("Your function should return a number", mode)
    elif not 1 <= result <= 20:
        fails("The result of the simulation should be between 1 and 20.", mode)
    else:
        ok(mode)
        
def check1_6(p_value, mode=CHECK):
    if not is_number(p_value):
        fails("Your answer should be a number", mode)
    elif not 0 < p_value < 1:
        fails("Your ansewr should be between 0 and 1", mode)
    else:
        ok(mode)
        
def check1_7(conclusion, mode=CHECK):
    check_multiple_choice_in_bounds(conclusion, 2, mode)
    
def check1_8(p_value_probability, mode=CHECK):
    check_multiple_choice_in_bounds(p_value_probability, 3, mode)
    
def check1_9(p_value_cutoff_probability, mode=CHECK):
    check_multiple_choice_in_bounds(p_value_cutoff_probability, 3, mode)
        
def check2_2(landing_test_statistic, mode=CHECK):
    result = landing_test_statistic(1, 1)
    if not is_number(result):
        fails("Your function should return a number", mode)
    elif result < 0:
        fails("Your function should return a positive number", mode)
    else:
        ok(mode)
        
def check3_3(probability_of_false, mode=CHECK):
    if not is_number(probability_of_false):
        fails("Your answer should be a number", mode)
    elif probability_of_false < 0:
        fails("Your answer should be a positive number", mode)
    elif probability_of_false > 1:
        fails("Probability should be no greater than 1", mode)
    else:
        ok(mode)
        
def check3_5(approximate_probability_of_false, mode=CHECK):
    if not is_number(approximate_probability_of_false):
        fails("Your answer should be a number", mode)
    elif approximate_probability_of_false < 0:
        fails("Your answer should be a positive number", mode)
    elif approximate_probability_of_false > 1:
        fails("Your answer should be no greater than 1", mode)
    else:
        ok(mode)
