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

def check1_4(mean_based_estimator, mode=CHECK):
    if not callable(mean_based_estimator):
        fails("Incorrect. Make sure you've used the right syntax to define the function.", mode)
    elif mean_based_estimator(np.array([1, 2, 3])) is None:
        fails("Incorrect, it looks like you forgot to return something.", mode)
    elif int(np.round(mean_based_estimator(np.array([1, 2, 3])))) != 4:
        fails('''It looks like your function doesn't compute the
        right estimate.  For consistency in the rest of the
        lab, it's best if you use the twice-the-mean estimate,
        even if you prefer some other estimate.''', mode)
    else:
        ok(mode)

def check1_5(max_estimate, mode=CHECK):
    if not is_number(max_estimate):
        fails("Incorrect. max_estimate should be a number.", mode)
    elif max_estimate != 135:
        fails("Incorrect. Make sure you return the maximum number in the sample.", mode)
    else:
        ok(mode)

def check2_1(one_resample, mode=CHECK):
    np.random.seed(123)
    if not is_table(one_resample):
        fails("Incorrect. Make sure your function returns a table.", mode)
    elif one_resample.num_rows != 17:
        fails("Incorrect. Make sure you sample `num_observations` rows of the data.", mode)
    elif one_resample['serial number'][5] != 42:
        fails("Incorrect. Make sure you are taking a random sample (and don't change our seed).", mode)
    else:
        ok(mode)

def check2_3(true_statements, mode=CHECK):
    if not is_iterable(true_statements):
        fails("Incorrect. Please make sure `true_statements` is a list.", mode)
    elif len(true_statements) != 2:
        fails("Incorrect. Check with a neighbor or TA to verify your answer.", mode)
    elif not is_number(true_statements[0]):
        fails("Incorrect. Please give a list of integers corresponding to the numbers of the true statements.", mode)
    elif not (1 in true_statements and 4 in true_statements):
        fails("Incorrect. Check with a neighbor or TA to verify your answer.", mode)
    else:
        ok(mode)

def check4_1(chebyshev_upper_limit, mode=CHECK):
    if not is_number(chebyshev_upper_limit):
        fails("Incorrect. Make sure `chebyshev_upper_limit` is a number.", mode)
    elif not is_close(chebyshev_upper_limit, 0.25):
        fails("Incorrect. Try again or ask a TA for help.", mode)
    else:
        ok(mode)

def check4_2(simulations, prob_winning, mode=CHECK):
    if not is_table(simulations):
        fails("Incorrect. `simulations` should be a table.", mode)
    elif simulations.num_rows != 50:
        fails("Incorrect. Make sure you simulate 50 tosses.", mode)
    elif not is_probability(prob_winning):
        fails("Incorrect. Make sure `prob_winning` is a probability.", mode)
    elif prob_winning > 0.1:
        fails("Incorrect. Your probability seems too high.", mode)
    else:
        ok(mode)
