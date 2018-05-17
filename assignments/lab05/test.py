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
        
#####################################################################################

def check1_1(number_cheese, mode=CHECK):
    if not is_number(number_cheese):
        fails('Incorrect. Your answer should be a number.', mode)
    elif number_cheese != 3:
        fails('Incorrect. Count the nachos with *only* cheese.', mode)
    else:
        ok(mode)

def check1_2(say_please, mode=CHECK):
    if not is_string_type(type(say_please)):
        fails('Incorrect. Your answer should be a string.', mode)
    elif say_please == '?':
        fails('Incorrect. Did you check if the number of cheesy nachos is less than 5?', mode)
    elif say_please != 'More please':
        fails('Incorrect. Make sure your condition is testing whether there are less than 5 nachos with cheese.', mode)
    else:
        ok(mode)

def check1_3(spicy_nacho, mode=CHECK):
    if not is_string_type(type(spicy_nacho)):
        fails('Incorrect. Your function should always return a string.', mode)
    elif spicy_nacho != 'Spicy!':
        fails('Incorrect. Make sure your function returns the correct string for each kind of nacho.', mode)
    else:
        ok(mode)


def check1_4(ten_nachos_reactions, mode=CHECK):
    if not check_table_labels(ten_nachos_reactions, ('Nachos', 'Reactions'),  mode):
        pass
    elif not np.count_nonzero(ten_nachos_reactions.column('Reactions') == make_array('Meh.', 'Cheesy!', 'Wow!', 'Wow!', 'Cheesy!', 'Spicy!', 'Wow!', 'Meh.', 'Cheesy!', 'Wow!')) == 10:
        fails('Incorrect. Make sure your `nacho_reaction` is correct for all inputs.', mode)
    else:
        ok(mode)


def check1_5(number_wow_reactions, mode=CHECK):
    if not is_number(number_wow_reactions):
        fails('Incorrect. Your answer should be a number.', mode)
    elif number_wow_reactions != 4:
        fails('Incorrect. Count the number of elements equal to "Wow!"', mode)
    else:
        ok(mode)

def check1_6(should_be_true, mode=CHECK):
    if not should_be_true:
        fails('Incorrect. Your expression should return True.', mode)
    else:
        ok(mode)

def check1_7(many_nachos, result, mode=CHECK):
    def both_or_neither(nacho_table):
        reactions = nacho_table.column('Reactions')
        number_wow_reactions = np.count_nonzero(reactions == 'Wow!')
        number_meh_reactions = np.count_nonzero(reactions == 'Meh.')
        if number_wow_reactions > number_meh_reactions:
            return 'Wow!'
        elif number_wow_reactions < number_meh_reactions:
            return 'Meh.'
        else:
            return 'Okay!'

    if not is_string_type(type(result)):
        fails('Incorrect. Your result should be a string', mode)
    elif not ((result == 'Wow!') or (result == 'Meh.') or (result == 'Okay!')):
        fails('Incorrect. Your result should be one of "Wow!", "Meh." or "Okay"', mode)
    elif not result == both_or_neither(many_nachos):
        fails('Incorrect. Your result does not match the expected result for this table.', mode)
    else:
        ok(mode)

def check2_1(total_score, mode=CHECK):
    if not is_number(total_score):
        fails('Incorrect. `total_score` should be a number.', mode)
    elif 1 < total_score < 10:
        fails('Incorrect. Your answer appears to be the result of a single dart toss. It should be the sum of 1000 tosses.', mode)
    elif total_score < 1000 or 10000 < total_score:
        fails('Incorrect. Your answer is outside the range of possible scores for 1000 tosses.', mode)
    elif total_score % 1000 == 0:
        passes('Your answer might be correct. Make sure, though, that you are generating a new random number for each toss. If you run the cell multiple times and always see this message, then your solution is incorrect.', mode)
    elif total_score < 3500 or 7500 < total_score:
        passes('Your answer might be correct, but the result is far from average. Try running the cell again to see if this message goes away.', mode)
    else:
        ok(mode)

def check2_2(total_score, average_score, mode=CHECK):
    if not is_number(average_score):
        fails('Incorrect. `average_score` should be a number.', mode)
    elif is_close(total_score / 1000, average_score):
        ok(mode)
    elif average_score == 5.5:
        fails("Your answer is most likely incorrect. It should be the average score of Clay's 1000 tosses from the previous question, not the expected score for any sequence of 1000 tosses.", mode)
    elif average_score < 1 or 10 < average_score:
        fails('Incorrect. Your answer should be the average points Clay earned for a single dart toss.', mode)
    else:
        fails_generic(mode)

def check2_3(longer_than_five, mode=CHECK):
    if not is_number(longer_than_five):
        fails('Incorrect. `longer_than_five` should be a number.', mode)
    elif longer_than_five == 48032:
        fails('Incorrect. Make sure that you are not counting words whose length is exactly five characters.', mode)
    elif longer_than_five != 35453:
        fails('Incorrect. Make sure you count only words longer than five characters.', mode)
    else:
        ok(mode)

def check2_4(chance_of_all_different, mode=CHECK):
    if not (is_number(chance_of_all_different) and 0 <= chance_of_all_different <= 1):
        fails('Incorrect. `chance_of_all_different` should be a probability (between 0 and 1).', mode)
    elif not 0.58 <= chance_of_all_different <= 0.68:
        fails('Incorrect. Your probability seems off.', mode)
    else:
        ok(mode)
        
def check2_5(num_wall, mode=CHECK):
    if not is_number(num_wall):
        fails('Incorrect. `num_wall` should be a number.', mode)
    elif not (0 <= num_wall <= 10):
        fails('Incorrect. John Wall cannot be in the team more than 10 times', mode)
    else:
        ok(mode)

def check3_1(pizza_prob, mode=CHECK):
    if not is_number(pizza_prob) or pizza_prob < 0 or 1 < pizza_prob:
        fails('Incorrect. `pizza_prob` should be a probability, i.e. a number between 0 and 1.', mode)
    elif is_close(pizza_prob, 0.3):
        fails('Incorrect. Remember, each dish has a 30% chance of *not* being available.', mode)
    elif not is_close(pizza_prob, 0.7):
        fails("Incorrect. We're looking for the probability that pizza will be available.", mode)
    else:
        ok(mode)

def check3_2(all_prob, mode=CHECK):
    if not is_number(all_prob) or all_prob < 0 or 1 < all_prob:
        fails('Incorrect. `all_prob` should be a probability, i.e. a number between 0 and 1.', mode)
    elif is_close(all_prob, 0.3 ** 4) or is_close(all_prob, 1 - 0.3 ** 4) or is_close(all_prob, 1 - 0.7 ** 4):
        fails('Incorrect. We are looking for the probability that all of the foods will be available. i.e. that enchiladas will be available *and* hamburgers, etc.', mode)
    elif not is_close(all_prob, 0.7 ** 4):
        fails_generic(mode)
    else:
        ok(mode)
 
def check3_3(something_is_out, mode=CHECK):
    if not is_number(something_is_out) or something_is_out < 0 or 1 < something_is_out:
        fails('Incorrect. `something_is_out` should be a probability, i.e. a number between 0 and 1.', mode)
    elif is_close(something_is_out, 0.3 ** 4) or is_close(something_is_out, 1 - 0.3 ** 4):
        fails('Incorrect. We are looking for the probability that at least one of the foods is unavailable.', mode)
    elif is_close(something_is_out, 0.7 ** 4):
        fails('Incorrect. This should be the probability that the foods are *not* all available.', mode)
    elif not is_close(something_is_out, 1 - 0.7 ** 4):
        fails_generic(mode)
    else:
        ok(mode)

def check3_4(winning_prob, mode=CHECK):
    if not is_number(winning_prob) or winning_prob < 0 or 1 < winning_prob:
        fails('Incorrect. `winning_prob` should be a probability, i.e. a number between 0 and 1.', mode)
    elif is_close(winning_prob, 4/6 * 2/6):
        fails('Incorrect. Remember, the marbles are not put back in the bag after they are drawn.', mode)
    elif is_close(winning_prob, 2/6 * 2/5 * 2/4):
        fails('Incorrect. Keep in mind that it does not matter which marble is drawn first.', mode)
    elif is_close(winning_prob, 2/5 * 2/4):
        fails('Incorrect. Remember that the second marble drawn can be either of two colors.', mode)
    elif not is_close(winning_prob, 1 * 4/5 * 2/4):
        fails_generic(mode)
    else:
        ok(mode)

