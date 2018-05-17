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

def ok(mode):
    passes('Ok.', mode)
        
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

###############################################################################################


def check1_1(standard_units,correlation, mode=CHECK):
    rand_col = np.random.normal(0, 1, 10)
    if not is_np_array(standard_units(np.arange(3))):
        fails("standard_units should return an array.", mode)
    elif not is_number(abs(correlation(Table().with_columns('a', rand_col,'b', rand_col)))):
        fails("correlation should return a number.",mode)
    else:
        ok(mode)


def check1_2(fit_line, mode=CHECK): 
    t = Table().with_columns(['x', [1.0, 2.0],'y',  [1.0, 2.0]])
    if is_number(fit_line(t)):
        fails("your slope and intercept should be numbers.", mode)
    else:
        ok(mode)


def check1_3(resample_slopes, mode=CHECK):
    if not is_np_array(resample_slopes):
        fails("resample_slopes should be an array", mode)
    else:
        ok(mode)

        
def check1_4(lower_end, upper_end, mode=CHECK):
    if not (is_number(lower_end) and is_number(upper_end)):
        fails("Your answer should be a number.", mode)
    else:
        ok(mode)


def check1_5(answer, mode=CHECK):
    check_multiple_choice_in_bounds(answer, 3, mode)


def check1_6(answer, mode=CHECK):
    if not is_number(answer):
        fails("Your function should return a number.", mode)
    else:
        ok(mode)


def check1_7(five_minutes_wait, mode=CHECK):
    if not is_number(five_minutes_wait):
        fails("Your function should return a number.", mode)
    else:
        ok(mode)


def check1_8(regression_lines, mode=CHECK):
    if not is_table(regression_lines):
        fails("Your function should return a table.", mode)
    else:
        ok(mode)


def check1_9(predictions_for_five, mode=CHECK):
    if not is_np_array(predictions_for_five):
        fails("predictions_for_five should be an array.", mode)
    else:
        ok(mode)


def check1_10(lower_bound, upper_bound, mode=CHECK):
    if not (is_number(lower_bound) and is_number(upper_bound)):
        fails("lower_bound or upper_bound should be a number.", mode)
    else:
        ok(mode)


def check2_1(answer, mode=CHECK):
    if not (is_np_array(answer)):
        fails("Your function should return an array.", mode)
    else:
        ok(mode)


def check2_3(answer, mode=CHECK):
    check_multiple_choice_in_bounds(answer, 4, mode)


def check2_5(boston_residual_sd, boston_residual_sd_from_formula, mode=CHECK):
    if not (is_number(boston_residual_sd) and is_number(boston_residual_sd_from_formula)):
        fails("boston_residual_sd or boston_residual_sd_from_formula should be a number.", mode)
    else:
        ok(mode)


def check2_6(faithful_residual_sd, faithful_residual_sd_from_formula, mode=CHECK):
    if not (is_number(faithful_residual_sd) and is_number(faithful_residual_sd_from_formula)):
        fails("faithful_residual_sd or faithful_residual_sd_from_formula should be a number.", mode)
    else:
        ok(mode)
