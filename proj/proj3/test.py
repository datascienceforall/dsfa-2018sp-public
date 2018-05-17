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

### Allow rounding of elipsis
def round(n, tol):
    if is_number(n):
        return np.round(n, tol)
    else:
        return 0

def check1_1(expected_row_sum, mode=CHECK):
    if not is_number(expected_row_sum):
        fails("Incorrect. `expected_row_sum` should be a number", mode)
    else:
        ok(mode)

def check1_1_1(percent_unchanged, mode=CHECK):
    if not is_number(percent_unchanged):
        fails("Incorrect. `percent_unchanged` should be a number.", mode)
    elif not (1 <= percent_unchanged <= 100):
        fails("Incorrect. `percent_unchanged` should be a percentage.", mode)
    else:
        ok(mode)

def check1_1_2(stemmed_message, mode=CHECK):
    if not is_string_type(type(stemmed_message)):
        fails("Incorrect. `stemmed_message` should be a string.", mode)
    elif not len(stemmed_message) < len('alternating'):
        fails("Incorrect. `stemmed_message` should be a substring of 'alternating'", mode)
    elif not 'alternating'.startswith(stemmed_message):
        fails("Incorrect. `stemmed_message` should be a substring of 'alternating'", mode)
    else:
        ok(mode)

def check1_1_3(unstemmed_run, mode=CHECK):
    if not is_np_array(unstemmed_run):
        fails("Incorrect. `unstemmed_run` should be an np.array.", mode)
    elif not unstemmed_run.item(0).startswith('run'):
        fails("Incorrect. All items should start with the substring `run`.", mode)
    elif len(unstemmed_run) <= 1:
        fails("Incorrect. `unstemmed_run` should have more than 1 element", mode)
    else:
        ok(mode)

def check1_1_4(most_shortened, mode=CHECK):
    if not is_string_type(type(most_shortened)):
        fails("Incorrect. `most_shortened` should be a string", mode)
    else:
        ok(mode)

def check2_1_1(romance_distance, mode=CHECK):
    if not is_number(romance_distance):
        fails("Incorrect. `romance_distance` should be a number", mode)
    elif not (0 < romance_distance < 1):
        fails("Incorrect. `romance_distance` should be between 0 and 1", mode)
    else:
        ok(mode)

def check2_1_2(distance_two_features, mode=CHECK):
    correct = 0.0011432060212606049
    dis = distance_two_features("titanic", "the avengers", "money", "feel")
    if not callable(distance_two_features):
        fails("Incorrect. `distance_two_features` should be a function.", mode)
    elif not is_number(dis):
        fails("Incorrect. `distance_two_features` should return a number", mode)
    elif not is_close(dis, correct):
        fails("Incorrect. `distance_two_features` returns an incorrect value.", mode)
    else:
        ok(mode)

def check2_1_3(distance_from_batman_returns, mode=CHECK):
    if not callable(distance_from_batman_returns):
        fails("Incorrect. `distance_from_batman_returns` should be a function.", mode)
    elif not is_number(distance_from_batman_returns('titanic')):
        fails("Incorrect. `distance_from_batman_returns` should return a number", mode)
    elif not np.isclose(distance_from_batman_returns('titanic'), 0.0023550202650824965):
        fails("Incorrect.", mode)
    else:
        ok(mode)

def check2_1_4(close_movies, mode=CHECK):
    if not check_table_labels(close_movies, ("Title", "Genre", "money", "feel", "distance"), mode):
        return
    elif close_movies.num_rows != 7:
        fails("Incorrect. `close_movies` should have 7 rows.", mode)
    else:
        ok(mode)
def check2_1_5(most_common, close_movies, mode=CHECK):
    correct =  ['romance', 'romance', 'romance', 'romance']
    if not callable(most_common):
        fails("Incorrect. `most_common` should be a function.", mode)
    elif not is_table(close_movies):
        fails("Incorrect. `close_movies` should be a table.", mode)
    elif not is_string_type(type(most_common('Genre', close_movies.take(range(2))))):
        fails("Incorrect. `most_common` should return a string.", mode)
    elif [most_common('Genre', close_movies.take(range(k))) for k in range(1, 8, 2)] != correct:
        fails("Incorrect.", mode)
    elif [most_common('Genre', close_movies.take(range(7-k, 7))) for k in range(1, 8, 2)] != correct:
        fails("Incorrect.", mode)
    else:
        ok(mode)

def check3_1(distance, distance_first_to_first, mode=CHECK):
    if not callable(distance):
        fails("Incorrect. `distance` should be a function.", mode)
    elif not is_number(distance_first_to_first):
        fails("Incorrect. The distance between two movies should be number.", mode)
    elif distance_first_to_first < 0:
        fails("Incorrect. The distance between two movies should be a positive number", mode)
    else:
        ok(mode)

def check_3_0_1(choice, mode=CHECK):
    check_multiple_choice_in_bounds(choice, 5, mode)

def check_3_0_1_4(choice, mode=CHECK):
    check_multiple_choice_in_bounds(choice, 2, mode)

def check3_1_1(my_20_features, mode=CHECK):
    if not is_np_array(my_20_features):
        fails("Your solution should be a numpy array.", mode)
    elif len(my_20_features) != 20:
        fails("Your solution should have 20 elements.", mode)
    elif not np.all([isinstance(f, str) for f in my_20_features]):
        fails("Your solution should only contain string..", mode)
    else:
        ok(mode)

def check3_1_3(genre_and_distances, mode=CHECK):
    if not is_table(genre_and_distances):
        fails("Your solution should be a table.", mode)
    else:
        ok(mode)

def check3_1_4(my_assigned_genre, my_assigned_genre_was_correct, mode=CHECK):
    if not isinstance(my_assigned_genre, str):
        fails("`my_assigned_genre` should be a string", mode)
    elif not isinstance(my_assigned_genre_was_correct, bool):
        fails("`my_assigned_genre_was_correct` should dbe a boolean", mode)
    else:
        ok(mode)

def check3_2(classify, mode=CHECK):
    if not callable(classify):
        fails("`classify` should be a function.", mode)
    else:
        ok(mode)

def check3_2_2(king_kong_genre, mode=CHECK):
    if not isinstance(king_kong_genre, str):
        fails("Your solution should be a string", mode)
    else:
        ok(mode)

def check3_2_3(classify_one_argument, test_20_0, mode=CHECK):
    ans = classify_one_argument(test_20_0)
    if not isinstance(ans, str):
        fails("Your function should return a string", mode)
    else:
        ok(mode)

def check3_3_1(proportion_correct, mode=CHECK):
    if not is_number(proportion_correct):
        fails("Your solution should be a number. ", mode)
    elif proportion_correct < 0 or proportion_correct > 1:
        fails("Your solution should be between 0 and 1.", mode)
    else:
        ok(mode)
