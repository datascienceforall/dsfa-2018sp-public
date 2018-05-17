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

def check1_1(c_lower_bound,c_upper_bound, mode=CHECK):
    if not (is_number(c_lower_bound) and is_number(c_upper_bound)):
        fails("Your answer is not a number.", mode)
    else: 
        ok(mode)


def check1_2(diff_lower_bound, diff_upper_bound, mode=CHECK):
    if not (is_number(diff_lower_bound) and is_number(diff_upper_bound)):
        fails("Your answer is not a number.", mode)
    else: 
        ok(mode)

def check2_1(ci_interpretation, mode=CHECK):
    check_multiple_choice_in_bounds(ci_interpretation, 6, mode)


def check2_2(new_samples_containing_true_proportion, mode=CHECK):
    check_multiple_choice_in_bounds(new_samples_containing_true_proportion, 4, mode)


def check2_3(intervals, mode=CHECK):
    if is_iterable(intervals) \
        and all(is_number(x) for x in intervals) \
        and is_close(sorted(intervals), [.8, .9, .99]).all():
        ok(mode)
    else:
        fails('Your answer must be a list containing the numbers .8, .9, and .99, though not necessarily in that order.', mode)


def check2_4(answer, mode=CHECK):
    check_multiple_choice_in_bounds(answer, 3, mode)


def check2_5(answer, mode=CHECK):
    check_multiple_choice_in_bounds(answer, 3, mode)


def check2_6(answer, mode=CHECK):
    check_multiple_choice_in_bounds(answer, 3, mode) 


def check3_1(grouped_mean, mode=CHECK):
    ages = Table().with_columns('age', [0, 1, 2, 3, 5, 6], 'count', [2, 5, 1, 4, 10, 1])
    if grouped_mean(ages) == -1:
        fails("Please replace [return -1] with your own code", mode)
    elif not (1 <= grouped_mean(ages) <= 5):
        fails("Your function doesn't seem to produce the right answer for the ages table", mode)
    else:
        ok(mode)

def check3_2(grouped_std, mode=CHECK):
    ages = Table().with_columns('age', [0, 1, 2, 3, 5, 6], 'count', [2, 5, 1, 4, 10, 1])
    if grouped_std(ages) == -1:
        fails("Please replace [return -1] with your own code", mode)
    elif not (1 <= grouped_std(ages) <= 10):
        fails("Your function doesn't seem to produce the right answer for the ages table", mode)
    else:
        ok(mode)

def check3_3(grouped_std_0, numpy_std_0, numpy_std_1, grouped_std_1, mode=CHECK):
    if not(is_number(grouped_std_0) and is_number(numpy_std_0)):
        fails("Either grouped_std_0 or numpy_std_0 is not a number", mode)
    elif not(is_number(grouped_std_1) and is_number(numpy_std_1)):
        fails("Either grouped_std_1 or numpy_std_1 is not a number", mode)
    else:
        ok(mode)


def check4_1(sample_size_n, mode=CHECK):
    if not is_np_array(sample_size_n(5)): 
        fails("Your function should return an array.", mode)
    else:
        ok(mode)


def check4_3(predict_sd, mode=CHECK):
    if predict_sd(5) == -1:
        fails("Please replace [return -1]", mode)
    else:
        ok(mode)


def check4_4(empirical_sd, mode=CHECK):
    if not is_number(empirical_sd(5)):
        fails("Your function should return a number", mode)
    else:
        ok(mode)


def check5_2(approximate_sd, mode=CHECK):
    if not is_number(approximate_sd):
        fails("Your answer is not a number.", mode)
    else:
        ok(mode)


def check5_3(exact_sd, mode=CHECK):
    if not is_number(exact_sd):
        fails("Your answer is not a number.", mode)
    else:
        ok(mode)


def check5_4(lower_limit, upper_limit, mode=CHECK):
    if not (is_number(lower_limit) and is_number(upper_limit)):
        fails("Your answer is not a number.", mode)
    else:
        ok(mode)

