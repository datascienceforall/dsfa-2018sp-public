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

def check_table_labels_sorted(table, labels_sorted, mode):
    if not is_table(table):
        fails('Incorrect. Your answer should be a table.', mode)
        return False
    elif tuple(sorted(table.labels)) != labels_sorted:
        fails('Incorrect. Double check your column labels.', mode)
        return False
    else:
        return True
        
###############################################################################################


def check1_1(answer, mode=CHECK):
    true_label = ('Age', 'Assists', 'Blocks', 'Games', 'Name', 'Points', 'Rebounds', 'Salary', 'Steals', 'Team', 'Turnovers')
    if not check_table_labels_sorted(answer, true_label, mode):
        pass
    else:
        ok(mode)


def check1_4(data_types, mode=CHECK):
    check_multiple_choice_in_bounds(data_types, 4, mode)


def check1_5(data_types, mode=CHECK):
    check_multiple_choice_in_bounds(data_types, 2, mode)


def check2_1(answer, mode=CHECK):
    if not is_number(answer):
        fails("Your answer is not a number.", mode)
    elif not answer > 0:
        fails("Your answer should be a positive number.", mode)
    elif answer > 0.5:
        fails("Your answer looks too large.", mode)
    else:
        ok(mode)


def check2_2(answer, mode=CHECK):
    if not is_number(answer):
        fails("Your answer is not a number.", mode)
    elif not int(answer) == answer:
        fails("Your answer is not an integer.", mode)
    elif not 20 < answer <= 100:
        fails("Your answer looks either too large or too small.", mode)
    else:
        ok(mode)


def check2_3(answer, mode=CHECK):
    if not is_number(answer):
        fails("Your answer is not a number.", mode)
    elif not 1e-8 < answer < 1e-6:
        fails("Your answer looks either too large or too small.", mode)
    else:
        ok(mode)


def check2_4(answer, mode=CHECK):
    if not isinstance(answer, list):
        fails("Your answer should be a list.", mode)
    elif not sorted(answer) == [1, 2, 3, 4, 5, 6, 7]:
        fails("Your list should contain the numbers 1 through 7.", mode)
    else:
        ok(mode)


def check3_2(get_day_in_month, mode=CHECK):
    check1 = get_day_in_month(315)
    check2 = get_day_in_month(415)
    if not is_number(check1): 
        fails("Incorrect. Your function should return a number", mode)
    elif not check1 == 15:
        fails("Incorrect. The day of date 315 should be 15.", mode)
    elif check2 == 115:
        fails("Incorrect. You should use remainder operator, instead of subtraction", mode)
    else:
        ok(mode)

def check3_3(missing, mode=CHECK):
    if not is_np_array(missing):
        fails("Incorrect. Your function should return an array", mode)
    else:
        number = len(missing)
        if number <= 25:
            fails("Incorrect. Not enough missing dates. You found only {} of them.".format(number),
                  mode)
        elif number >= 35:
            fails("Incorrect. Too many missing dates. You found {} of them.".format(number),
                  mode)
        elif 14 not in missing:
            fails("Incorrect. 14 is a missing date but you did not find it.",
                  mode)
        elif 85 not in missing:
            fails("Incorrect. 85 is a missing date but you did not find it.",
                  mode)
        else:
            ok(mode)

def check3_4(pred, mode=CHECK):
    if not is_number(pred): 
        fails("Incorrect. Your prediction should be a number", mode)
    elif not 65 < pred < 75: 
        fails("Incorrect. Your prediction is inaccurate. Did you get the day of the year right?", mode) 
    else:
        ok(mode)


