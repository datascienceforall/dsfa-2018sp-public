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


def check1_1(answer, mode=CHECK):
    if not type(answer) == list:
        fails("Your answer is not a list.", mode)
    else: 
        ok(mode)


def check1_2(answer, mode=CHECK):
    if not is_table(answer):
        fails("Your answer is not a table", mode)
    elif not answer.labels != ('Year', 'Murder rate in Minnesota', 'Murder rate in Alaska'):
        fails("Your labels are not in the right order.", mode)
    elif not answer.num_rows == 44:
        fails("The number of rows in your table is incorrect", mode)
    else:
        ok(mode)


def check1_3(most_murderous, mode=CHECK):
    import matplotlib.pyplot as plots
    try:
        if is_number(most_murderous(1970)):
            fails("You should replace return = 0.", mode)
        elif not isinstance(most_murderous(1970).item(0), str):
            fails("The names of the states should have type string",mode)
        elif not len(most_murderous(1970)) == 5:
            fails("Your function does not return the 5 states that had the highest murder rate in a given year", mode)
        else:
            ok(mode)
    finally:
        plots.close('all')


def check1_4(ca_change, mode=CHECK):
    if not is_number(ca_change):
        fails("Your answer is not a number", mode)
    elif not ca_change > 0:
        fails("You might have flipped the difference.",mode)
    else:
        ok(mode)


def check2_1(two_year_changes, mode=CHECK):
    # count when there is no difference 
    no_diff1 = two_year_changes(make_array(10, 7, 12, 9, 13, 9, 11)) != 3
    no_diff2 = two_year_changes(make_array(10, 7, 12, 9, 13, 9, 11)) != 1
    if not (no_diff1 and no_diff2):
        fails("Don't count cases where the number stays the same as either an increase or a decrease.", mode)
    elif not two_year_changes(make_array(10, 7, 12, 9, 13, 9, 11)) != -2:
        fails("You might have flipped the difference.", mode)
    else:
        ok(mode)


def check2_2(changes_by_state, mode=CHECK):
    if not is_table(changes_by_state):
        fails("Your answer is not a table", mode)
    elif not changes_by_state.num_rows == 50:
        fails("The number of rows is not correct",mode)
    elif not list(changes_by_state.row(0)) == ['Alabama', -6]:
        fails("Alabama's two year murder rate change should be -6", mode)
    elif not list(changes_by_state.row(1)) == ['Alaska', -5]:
        fails("Alaska's two year murder rate change should be -5", mode)
    else:
        ok(mode) 


def check2_3(total_changes, mode=CHECK):
    if not is_number(total_changes):
        fails("Your answer is not a number", mode)
    elif not 0 < total_changes:
        fails("Your answer should be positive",mode)
    else:
        ok(mode)


def check2_4(num_changes, mode=CHECK):
    if not is_number(num_changes):
        fails("Your answer is not a number.", mode)
    elif not num_changes != 50:
        fails("There are several two-year changes for each state.", mode)
    elif 42 <= num_changes <= 44:
        fails("The entire data set contains many states, not just 1.", mode)
    elif not 2000 <= num_changes <= 2200:
        fails("Your answer doesn't seem to be in the correct range.", mode)
    else:
        ok(mode)


def check2_6(which_side, reject_null, mode=CHECK):
    if not reject_null in [False, True]:
        fails("reject_null should be a boolean", mode)
    elif not which_side in ["Right", "Left"]:
        fails("which_side should be either \"Right\" or \"Left\". ", mode)
    else:
        ok(mode)


def check3_3(answer, mode=CHECK):
    if not is_table(answer):
        fails("Your answer is not a table", mode)
    elif not answer.num_rows == 1936:
        fails("The number of rows in your table is incorrect", mode)
    else:
        ok(mode)


def check3_4(answer, mode=CHECK):
    if not is_number(answer):
        fails("Your answer should be a number.", mode)
    else:
        ok(mode)


def check4_1(run_test, murder_rates, mode=CHECK):
    if not callable(run_test):
        fails("Incorrect. Make sure you've used the right syntax to define the function.", mode)
        return
    p_val = run_test(murder_rates, 1960)
    if p_val == None:
        fails("Incorrect. Make sure you used the return keyword in your function.", mode)
    elif not is_number(p_val):
        fails("Incorrect. Make sure your function returns a number.", mode)
    elif not (0.0 <= p_val <= 0.05):
        fails("Incorrect. The P-value for murder_rates starting in 1960 is far from expected.", mode)
    else:
        ok(mode)

def check4_2(non_death_penalty_murder_rates, mode=CHECK):
    if not check_table_labels(non_death_penalty_murder_rates, ('State', 'Year', 'Population', 'Murder Rate'), mode):
        return
    if non_death_penalty_murder_rates.num_rows != 264:
        fails("Incorrect. Make sure your table only contains rows from non-death-penalty states.", mode)
    else:
        ok(mode)

def check4_3(we_conclude, mode=CHECK):
    if not we_conclude in [1, 2, 3, 4, 5]:
        fails("Incorrect. we_conclude should be a number 1-5, corresponding to one of the statements listed above.", mode)
    else:
        ok(mode)

def check5_1(average_murder_rates, mode=CHECK):
    if not check_table_labels(average_murder_rates, ('Year', 'Death penalty states', 'No death penalty states'), mode):
        return
    if average_murder_rates.num_rows != 44:
        fails("Incorrect. The table should include every year in murder_rates.", mode)
    elif not np.isclose(average_murder_rates.column(1).item(3), 4.6, rtol=1e-01):
        fails("Incorrect. The average murder rate for death penalty states in 1963 should be about 4.6.", mode)
    else:
        ok(mode)
