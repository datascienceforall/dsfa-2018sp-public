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

def normalize_bool(b):
    return True if b else False

def is_probability(x):
    return is_number(x) and 0 <= x <= 1

##################################################

def check1_3(duration_mean, duration_std, wait_mean, wait_std, faithful_standard, mode=CHECK):
    if not (is_number(duration_mean) and is_number(duration_std) and is_number(wait_mean) and is_number(wait_std)):
        fails("Incorrect. The means and standard deviations should be numbers.", mode)
    elif not np.isclose(duration_mean, 3.488, rtol=1e-3):
        fails("Incorrect. Make sure `duration_mean` is the mean duration of the geyser.", mode)
    elif not np.isclose(duration_std, 1.139, rtol=1e-3):
        fails("Incorrect. Make sure `duration_std` is the standard deviation of the geyser durations.", mode)
    elif not np.isclose(wait_mean, 70.897, rtol=1e-3):
        fails("Incorrect. Make sure `wait_mean` is the mean waiting time of the geyser.", mode)
    elif not np.isclose(wait_std, 13.570, rtol=1e-3):
        fails("Incorrect. Make sure `wait_std` is the standard deviation of the geyser waiting times.", mode)
    elif not is_table(faithful_standard):
        fails("Incorrect. `faithful_standard` should be a table.", mode)
    elif abs(sum(faithful_standard.column(0))) > 1e-8:
        fails("Incorrect. Make sure the values in `faithful_standard` are in standard units.")
    else:
        ok(mode)

def check1_5(correlation_guess, mode=CHECK):
    if correlation_guess not in [-1, 0, 1]:
        fails("Incorrect. Your guess should be -1, 0, or 1.", mode)
    elif correlation_guess != 1:
        fails("Incorrect. Check with a neighbor or TA to verify your answer.", mode)
    else:
        ok(mode)

def check1_6(r, mode=CHECK):
    if not is_number(r):
        fails("Incorrect. `r` should be a number.", mode)
    elif not np.isclose(r, 0.901, rtol=1e-3):
        fails("Incorrect. Make sure you have the correct definition for the correlation.", mode)
    else:
        ok(mode)

def check2_3(bootstrap_sampled_SD, mode=CHECK):
    if bootstrap_sampled_SD not in [1, 2, 3, 4]:
        fails("Incorrect. `bootstrap_sampled_SD` should be a number 1–4, corresponding to the correct answer above.", mode)
    elif bootstrap_sampled_SD != 3:
        fails("Incorrect. Check with a neighbor or TA to verify your answer.", mode)
    else:
        ok(mode)

def check2_4(pop_vs_sample, mode=CHECK):
    if pop_vs_sample not in [1, 2, 3, 4]:
        fails("Incorrect. `pop_vs_sample` should be a number 1–4, corresponding to the correct answer above.", mode)
    elif pop_vs_sample != 3:
        fails("Incorrect. Check with a neighbor or TA to verify your answer.", mode)
    else:
        ok(mode)

