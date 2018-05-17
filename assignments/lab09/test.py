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


def check1_3(driving_start_time_hours,  mode=CHECK):
    if not is_number(driving_start_time_hours):
        fails("Incorrect. Your answer should be a number", mode)
    elif abs(driving_start_time_hours - 5/3) > 4/9:
        fails("Incorrect. It looks like your answer is very far from the right one.", mode)
    elif 1/9 < abs(driving_start_time_hours - 5/3) < 4/9:
        fails(
            '''Incorrect. It looks like your answer is in the ballpark, but
            not quite right.  Hint: Try finding a place where
            the line intersects a crossing of two grid lines.''', mode)
    else:
        ok(mode)

def check1_4(first_guess, mode=CHECK):
    if not is_number(first_guess):
        fails("Incorrect. Your guess should be a number", mode)
    elif first_guess < 1e6:
        fails("Incorrect. Make sure your units are correct.", mode)
    elif not(10*10**9 <= first_guess <= 20*10**9):
        fails("Incorrect. Check with a TA for help.", mode)
    else:
        ok(mode)

def check1_5(errors, mode=CHECK):
    tbl = Table().with_columns(["Speed (parsecs/year)", [1, 2, 3, 4], "Distance (million parsecs)", [2, 4, 6, 8]])
    correct_err = np.array([0, 1, 2, 3])
    if not callable(errors):
        fails("Incorrect. `errors` should be a function.", mode)
    elif is_table(errors(tbl, 1, 1)):
        fails("Incorrect. Your function should return an array, not a table", mode)
    elif not is_iterable(errors(tbl, 1, 1)):
        fails("Incorrect. Your function should return an array", mode)
    elif is_close(errors(tbl, 1, 1)[1], -1):
        fails("Incorrect. You may be calculating the error backwards.", mode)
    elif not np.all(is_close(correct_err, abs(np.array(errors(tbl, 1, 1))))):
        fails("Incorrect. Your function does not seem to produce the correct errors. Please check with a TA.", mode)
    else:
        ok(mode)

def check1_6(example_errors, mode=CHECK):
    if not is_np_array(example_errors):
        fails("Incorrect. `example_errors` should be a numpy array.", mode)
    elif not np.isclose(example_errors.item(0), -22.43, rtol=1e-2):
        fails("Incorrect. Make sure you are calculating the errors correctly", mode)
    else:
        ok(mode)

def check1_7(fit_line, mode=CHECK):
    example_table = Table().with_columns(
        "Speed (parsecs/year)", make_array(0, 1),
        "Distance (million parsecs)", make_array(1, 3))
    if not callable(fit_line):
        fails("Incorrect. `fit_line` should be a function.", mode)
    elif not is_np_array(fit_line(example_table)):
        fails("Incorrect, your function should return a numpy array of the form make_array(slope, intercept)", mode)
    elif np.all(abs(fit_line(example_table) - make_array(1, 2)) < .5):
        fails("Incorrect, you don't seem to have the correct slope and intercept. Make sure your array has slope first, then intercept.", mode)
    elif not np.all(abs(fit_line(example_table) - make_array(2, 1)) < .5):
        fails("Incorrect, you don't seem to have the correct slope and intercept. See a TA for help.", mode)
    else:
        ok(mode)

def check1_9(lower_end, upper_end, mode=CHECK):
    if not is_number(lower_end) or not is_number(upper_end):
        fails("Incorrect. `upper_end` and `lower_end` should be numbers.", mode)
    elif not (abs(upper_end/1e9 - 14.5) < .3 and abs(lower_end/1e9 - 13.5) < .3):
        fails("Incorrect. Your confidence interval seems wrong, see a TA for help.", mode)
    else:
        ok(mode)
