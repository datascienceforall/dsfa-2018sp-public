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

def check1_1(possible_rolls, roll_result, modified_result, action_succeeded, mode=CHECK):
    if not (is_iterable(possible_rolls) and is_number(roll_result) and is_number(modified_result)):
        fails("Incorrect. Make sure possible_rolls is an array, and the results are numbers.", mode)
    elif len(possible_rolls) != 20 or not all(map(lambda x: x in possible_rolls, np.arange(1, 21, 1))):
        fails("Incorrect. Make sure possible_rolls contains exactly the values 1-20.", mode)
    elif not roll_result in np.arange(1, 21, 1):
        fails("Incorrect. Make sure roll_result is a random possible roll.", mode)
    elif roll_result + 11 != modified_result:
        fails("Incorrect. Make sure you're applying the correct modifier (+11) to the roll.", mode)
    elif normalize_bool(action_succeeded) != (modified_result > 15):
        fails("Incorrect. The action should succeed if the modified result is more than 15.", mode)
    else:
        ok(mode)

def check1_2(rough_success_chance, mode=CHECK):
    if not is_probability(rough_success_chance):
        fails('Incorrect. rough_success_chance should be a probability (between 0 and 1).', mode)
    else:
        ok(mode)

def check1_3(simulate_observations, mode=CHECK):
    if not callable(simulate_observations):
        fails("Incorrect. Make sure you've used the right syntax to define the function.", mode)
        return
    obs = simulate_observations()
    if not (is_iterable(obs) and all(map(is_number, obs))):
        fails("Incorrect. simulate_observations should return an array of numbers.", mode)
    elif len(obs) != 7:
        fails("Incorrect. observations should contain the results of 7 modified die rolls.", mode)
    elif not all(map(lambda x: 12 <= x < 32, obs)):
        fails("Incorrect. All observations should be within the possible range of modified rolls.", mode)
    else:
        obs = [simulate_observations() for _ in range(5000)]
        check_bool_ask_if_err(abs(5.7 - np.std(obs)) < .2 and abs(21.5 - np.mean(obs)) < .2, mode)

def check1_5(observations, min_estimate, mode=CHECK):
    if not is_number(min_estimate):
        fails("Incorrect. min_estimate should be a number.", mode)
    elif min_estimate == min(observations):
        fails("Incorrect. Remember, each roll will always be at least one more than the modifier.", mode)
    elif min_estimate != min(observations) - 1:
        fails("Incorrect. Make sure you are using the smallest roll in `observations` to make your estimate.", mode)
    else:
        ok(mode)

def check1_6(observations, mean_based_estimator, mode=CHECK):
    def reasonable_for(a):
        return abs(11 - (np.mean(a) - mean_based_estimator(a))) < 4
    arr1 = make_array(1, 2, 3, 4, 5, 6, 7)
    arr2 = make_array(5, 4, 3, 6, 7, 1, 4, 12, 8)
    if not check_fruitful_function(mean_based_estimator, arr1, mode):
        return
    if not is_number(mean_based_estimator(arr1)):
        fails("Incorrect. Your function should return a number.", mode)
    elif mean_based_estimator(arr1) == np.mean(arr1):
        fails("Incorrect. Make sure you are estimating the modifier, and not the average total roll.", mode)
    elif not reasonable_for(observations):
        fails_generic(mode)
    elif not (reasonable_for(arr1) and reasonable_for(arr2)):
        fails("Incorrect. Your function works correctly for `observations`, but not for other data sets.", mode)
    else:
        ok(mode)

def check2_1(full_data, histograms, mode=CHECK):
    import matplotlib.pyplot as plots
    try:
        if not callable(histograms):
            fails("Incorrect. Make sure you've used the right syntax to define the function.", mode)
            return
        bins = histograms(full_data)
        old = full_data.with_column('Age', full_data.column('Age')*3)
        if not is_iterable(bins):
            fails("Incorrect. Make sure your function returns an array.", mode)
        elif np.max(histograms(old)) <= np.max(old.column('Age')):
            fails("Incorrect.", mode)
        else:
            ok(mode)
    finally:
        plots.close('all')

def check2_2(full_stats, mode=CHECK):
    if not is_iterable(full_stats):
        fails("Incorrect. Make sure your function returns an array.", mode)
    elif not np.isclose(full_stats[0], 26.54, rtol=1e-02):
        fails("Incorrect. Make sure the first element in the returned array is the average age.", mode)
    elif not np.isclose(full_stats[1], 4269775.77, rtol=1e-02):
        fails("Incorrect. Make sure the second element in the returned array is the average salary.", mode)
    else:
        ok(mode)

def check2_3(convenience_sample, mode=CHECK):
    if not is_table(convenience_sample):
        fails("Incorrect. convenience_sample should be a table.",  mode)
    elif convenience_sample.num_columns != 11:
        fails("Incorrect. Make sure your sample contains all the columns of the full data.", mode)
    elif 44 < convenience_sample.num_rows:
        fails("Incorrect. Make sure your sample includes only players under 22.", mode)
    elif convenience_sample.num_rows < 44:
        fails("Incorrect. Make sure your sample includes all players under 22.", mode)
    else:
        ok(mode)

def check2_4(convenience_stats, mode=CHECK):
    if not is_iterable(convenience_stats):
        fails("Incorrect. Make sure you are using your compute_statistics function.", mode)
    elif not (np.isclose(convenience_stats[0], 20.36, rtol=1e-02) and np.isclose(convenience_stats[1], 2383533.82, rtol=1e-02)):
        fails("Incorrect. Make sure you are only computing statistics for the convenience sample.", mode)
    else:
        ok(mode)

def check2_6(small_stats, large_stats, mode=CHECK):
    if not (is_iterable(small_stats) and is_iterable(large_stats)):
        fails("Incorrect. Make sure you are using your compute_statistics function.", mode)
    elif not (np.isclose(small_stats[0], 26.32, rtol=1e-02) and np.isclose(small_stats[1], 4283910.89, rtol=1e-02)):
        fails("Incorrect. Your small_stats seem off. Make sure you are importing it from the provided CSV file.", mode)
    elif not (np.isclose(large_stats[0], 26.42, rtol=1e-02) and np.isclose(large_stats[1], 4821322.5, rtol=1e-02)):
        fails("Incorrect. Your large_stats seem off. Make sure you are importing it from the provided CSV file.", mode)
    else:
        ok(mode)
