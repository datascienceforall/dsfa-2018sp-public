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
def check1_2(spreads_around_5, spread_5_outcome_average, mode=CHECK):
    if not is_table(spreads_around_5):
        fails("spreads_around_5 should be a table.", mode)
    elif not is_number(spread_5_outcome_average):
        fails("spread_5_outcome_average should be a number.", mode)
    elif spread_5_outcome_average < 0:
        fails("spread_5_outcome_average should be a positive number.", mode)
    else:
        ok(mode)

def check1_3(expected_slope_for_equal_spread, expected_intercept_for_equal_spread, mode=CHECK):
    if not is_number(expected_slope_for_equal_spread) and not is_number(expected_intercept_for_equal_spread):
        fails("Both expected slope and expected intercept should be numbers.", mode)
    elif not -2 <= expected_slope_for_equal_spread <= 2 and \
         not -2 <= expected_intercept_for_equal_spread <= 2:
        fails("Both expected slope and expected intercept should be between -2 and 2.", mode)
    else:
        ok(mode)

def check1_4(standard_units, mode=CHECK):
    sample = [2, 0, 3, 6, 4]
    result = standard_units(sample)
    if not is_np_array(result):
        fails("Your function should return a numpy array.", mode)
    elif len(result) != len(sample):
        fails("The array returned by your function should have same length as the input.", mode)
    else:
        ok(mode)

def check1_5(spread_r, mode=CHECK):
    if not is_number(spread_r):
        fails("Your solution should be a number.", mode)
    elif abs(spread_r) > 1:
        fails("Your solution should be between -1 and 1.", mode)
    else:
        ok(mode)

def check1_6(spread_slope, mode=CHECK):
    if not is_number(spread_slope):
        fails("Your answer should be a number.", mode)
    elif not 0 <= spread_slope < 1:
        fails("Your answer should be between 0 and 1.", mode)
    else:
        ok(mode)

def check1_7(slope_implies_average_spread_above_average_outcome, mode=CHECK):
    if not isinstance(slope_implies_average_spread_above_average_outcome, bool):
        fails("Your answer should be an boolean. ", mode)
    else:
        ok(mode)
        
def check2_4(point_influence, mode=CHECK):
    if not isinstance(point_influence, int):
        fails("Your answer should be integer.", mode)
    else:
        check_multiple_choice_in_bounds(point_influence, 2, mode)
        
def check2_5(total_squared_error, mode=CHECK):
    arg = (0, 0)
    out = total_squared_error(*arg)
    if not is_number(out):
        fails("Your function should return a number.", mode)
    elif out < 0:
        fails("Squared error should be greater than 0.", mode)
    else:
        ok(mode)

def check2_6(eyeballed_error, aided_error, mode=CHECK):
    if not is_number(eyeballed_error) or not is_number(aided_error):
        fails("Both errors should be numbers.", mode)
    elif eyeballed_error > 14:
        fails("Eyeballed error is too large.", mode)
    elif aided_error > 14:
        fails("Aided error is too large", mode)
    else:
        ok(mode)

def check2_7(slope_from_minimize, intercept_from_minimize, mode=CHECK):
    if not is_number(slope_from_minimize) or not is_number(intercept_from_minimize):
        fails("Both slope and intercept should be numbers.", mode)
    elif not -1 <= slope_from_minimize <= 0:
        fails("Minimized slope should be between -1 and 0.", mode)
    elif not 0 <= intercept_from_minimize <= 2:
        fails("Minimized intercept should be between 0 and 2.", mode)
    else:
        ok(mode)

def check2_8(best_total_squared_error, mode=CHECK):
    if not is_number(best_total_squared_error):
        fails("The best total error should be a number.", mode)
    elif best_total_squared_error < 0:
        fails("The best total error should be positive.", mode)
    else:
        ok(mode)
        
def check3_2(correlation_coefficient_choice, mode=CHECK):
    if not isinstance(correlation_coefficient_choice, int):
        fails("Your answer should be an int.", mode)
    else:
        check_multiple_choice_in_bounds(correlation_coefficient_choice, 6, mode)

def check3_3(parameters, mode=CHECK):
    if not is_np_array(parameters):
        fails("Your answer should return a numpy array.", mode)
    elif len(parameters) != 3:
        fails("The output of your function should contains 3 parameters.", mode)
    elif not is_number(parameters.item(0)) or \
         not is_number(parameters.item(1)) or \
         not is_number(parameters.item(2)): 
        fails("All parameters should be numbers.", mode)
    else:
        ok(mode)

def check3_4(triple_record_vert_est, mode=CHECK):
    if not is_number(triple_record_vert_est):
        fails("Your answer should be a number.", mode)
    elif triple_record_vert_est <= 0:
        fails("Your answer should be greater than 0.", mode)
    elif not 100 <= triple_record_vert_est <= 200:
        fails("Your answer should be between 100 and 200.", mode)
    else:
        ok(mode)

def check4_3(resampled_means, mode=CHECK):
    if not is_np_array(resampled_means):
        fails("Your answer should be an numpy array.", mode)
    elif len(resampled_means) != 5000:
        fails("Your answer should contain 5000 elements", mode)
    else:
        ok(mode)

def check4_4(lower_bound,upper_bound, mode=CHECK):
    if not is_number(lower_bound) or not is_number(upper_bound):
        fails("Both bounds should be numbers", mode)
    elif lower_bound < 0 or upper_bound < 0:
        fails("Both bounds should be positive numbers.", mode)
    else:
        ok(mode)

def check4_7(lower_bound_normal, upper_bound_normal, mode=CHECK):
    if not is_number(lower_bound_normal) or not is_number(upper_bound_normal):
        fails("Both bounds should be numbers.", mode)
    elif lower_bound_normal < 0 or upper_bound_normal < 0:
        fails("Both bounds should be positive numbers.", mode)
    else:
        ok(mode)

