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

def check1(best_attribute, mode=CHECK):
    if not(is_string_type(type(best_attribute))):
        fails("Your answer should be a string.", mode)
    elif best_attribute not in ['carat', 'depth', 'table']:
        fails("Your answer should be either carat, depth, or table.", mode)
    elif best_attribute != 'carat':
        fails("That is not the best attribute.", mode)
    else:
        ok(mode)  

def check2(diamonds_1000, diamonds_mlr, diamonds, mode=CHECK):
    if not check_table_labels(diamonds_1000, diamonds.labels, mode):
        pass
    elif diamonds_1000.num_rows != 1000:
        fails('diamonds_1000 should have 1000 rows.', mode)
    elif not check_table_labels(diamonds_mlr, ('carat', 'depth', 'table', 'price'), mode):
        pass
    elif diamonds_mlr.num_rows != 1000:
        fails("diamonds_mlr should have 1000 rows.", mode)
    else:
        ok(mode) 
        
def check3(my_weights, first_row_attributes, first_row_prediction, diamonds_mlr, mode=CHECK):
    if not is_np_array(my_weights):
        fails('my_weights should be an array.', mode)
    elif not len(my_weights) == 4:
        fails('my_weights should have four elements.', mode)
    elif not is_np_array(first_row_attributes):
        fails('first_row_attributes should be an array.', mode)
    elif not len(first_row_attributes) == 3:
        fails('first_row_attributes should have three elements.', mode)
    elif not is_number(first_row_prediction):
        fails('first_row_prediction should be a number.', mode)
    elif mode==CHECK and not np.abs(diamonds_mlr.column('price').item(0) - first_row_prediction) <= 101:
        fails('Your prediction is not within $100 of the actual price. Try improving the weights you chose.', mode)
    else:
        ok(mode)
        
def check4(predict, table_with_mlr_predictions, my_predictions, my_weights, mode=CHECK):
    t = Table().with_columns('x', 100, 'y', 110)
    
    if not callable(predict):
        fails('predict should be a function.', mode)
    elif predict(make_array(1, 10), make_array(100)) != 110:
        fails('Your predict function doesn\'t correctly implement the multiple linear regression equation.', mode)
    elif not callable(table_with_mlr_predictions):
        fails('table_with_mlr_predictions should be a function.', mode)
    elif not is_table(table_with_mlr_predictions(t, 'y', make_array(1, 10))):
        fails('table_with_mlr_predictions should return a table.', mode)
    elif 'predicted y' not in table_with_mlr_predictions(t, 'y', make_array(1, 10)).labels:
        fails('table_with_mlr_predictions should add a column of predictions with the correct label.', mode)
    elif table_with_mlr_predictions(t, 'y', make_array(1, 10)).column('predicted y').item(0) != 110:
        fails('table_with_mlr_predictions doesn\'t compute the predictions correctly.', mode)
    elif not check_table_labels(my_predictions, ('carat', 'depth', 'table', 'price', 'predicted price'), mode):
        pass
    elif np.sum(my_weights * np.append(np.array(my_predictions.select(0,1,2).row(0)), 1)) != my_predictions.column('predicted price').item(0):
        fails('my_predictions does not contain the correct predicted values.', mode)
    else:
        ok(mode)
    
def check5(my_rmse, my_predictions, mode=CHECK):
    if not is_number(my_rmse):
        fails('Your answer should be a number.', mode)
    else:
        residuals = my_predictions.column('price') - my_predictions.column('predicted price')
        correct_rmse = np.sqrt(np.mean(residuals ** 2))
        if my_rmse != correct_rmse:
            fails('Incorrect. Double check how you are computing RMSE.', mode)
        else:
            ok(mode)
            
def check6(diamonds_mlr_rmse, my_weights, my_rmse, diamonds_mlr, mode=CHECK):
    if not callable(diamonds_mlr_rmse):
        fails('diamonds_mlr_rmse should be a function', mode)
    elif diamonds_mlr_rmse(my_weights) != my_rmse:
        fails('You don\'t seem to have the same RMSE as the previous question. Double check how you are computing RMSE in diamonds_mlr_rmse.', mode)
    elif diamonds_mlr_rmse(np.zeros(len(my_weights))) != np.sqrt(np.mean(diamonds_mlr.column('price')**2)):
        fails('diamonds_mlr_rmse doesn\'t seem to be computing RMSE correctly.', mode)
    else:
        ok(mode)
    
def check7(best_weights_mlr, diamonds_mlr, diamonds_mlr_rmse, mode=CHECK):
    if not is_np_array(best_weights_mlr):
        fails('Your answer should be an array.', mode)
    elif len(best_weights_mlr) != diamonds_mlr.num_columns:
        fails('Your array does not have the correct number of elements.', mode)
    elif diamonds_mlr_rmse(best_weights_mlr) >= diamonds_mlr_rmse(best_weights_mlr + 10):
        fails('The weights you found are not the best possible weights according to your diamonds_mlr_rmse function. Double check how you are minimizing.', mode)
    else:
        ok(mode)

def check8(categories, mode=CHECK):
    t = Table().with_columns('x', make_array('Heads', 'Tails', 'Tails'))
    if not callable(categories):
        fails('Your answer should be a function.', mode)
    elif not is_np_array(categories(t,'x')):
        fails('Your function should return an array.', mode)
    elif len(categories(t, 'x')) != 2:
        fails('There should not be any duplicates in the array your function returns. Make sure you are returning only the distinct values.', mode)
    elif set(categories(t, 'x')) != set(['Heads', 'Tails']):
        fails_generic(mode)
    else:
        ok(mode)
    
def check9(coding_of_value, mode=CHECK):
    a = make_array('Heads', 'Heads', 'Tails')
    if not callable(coding_of_value):
        fails('Your answer should be a function.', mode)
    else:
        coded = coding_of_value(a, 'Tails')
        if not is_np_array(coded):
            fails('Your function should return an array.', mode)
        elif len(coded) != len(a):
            fails('Your function should return an array of the same length as the array it receives as input.', mode)
        elif not issubclass(coded.dtype.type, np.integer):
            fails("Your function should return an array containing only integers.", mode)
        elif not (coded.min() == 0 and coded.max() == 1):
            fails("Your function should return an array containing only 0's and 1's.", mode)
        elif list(coded) != [0, 0, 1]:
            fails_generic(mode)
        else:
            ok(mode)
            
def check10(dummy_code, mode=CHECK):
    t = Table().with_columns('x', make_array('Heads', 'Heads', 'Tails'))
    
    if not callable(dummy_code):
        fails('Your answer should be a function.', mode)
    else:
        d = dummy_code(t, 'x')
        if not is_table(d):
            fails('Your function should return a table.', mode)
        elif not set(d.labels) == set(['x', 'Heads', 'Tails']):
            fails('Your function does not return a table with the correct column labels.', mode)
        elif list(d.column('Heads')) != [1, 1, 0] and list(d.column('Tails')) != [0,0,1]:
            fails('Your function does not dummy code the variables correctly.', mode)
        else:
            ok(mode)
    
def check11(diamonds_1000_dummy, mode=CHECK):
    correct_labels = ('carat','cut','color','clarity','depth',
     'table','price','Fair','Good','Ideal','Premium','Very Good',
     'I1','IF','SI1','SI2','VS1','VS2','VVS1','VVS2','D','E','F',
     'G','H','I','J')
    
    if not is_table(diamonds_1000_dummy):
        fails('Your answer should be a table.', mode)
    elif set(diamonds_1000_dummy.labels) != set(correct_labels):
        fails('Your table does not contain the correct columns.', mode)
    else:
        d0 = diamonds_1000_dummy.row(0)
        if d0.item(d0.item('cut')) != 1:
            fails('Your table does not correctly dummy-code cut.', mode)
        elif d0.item(d0.item('color')) != 1:
            fails('Your table does not correctly dummy-code color.', mode)
        elif d0.item(d0.item('clarity')) != 1:
            fails('Your table does not correctly dummy-code clarity.', mode)
        else:
            ok(mode)
    
def check12(diamonds_4cs_rmse, some_arbitrary_weights, diamonds_4cs, mode=CHECK):
    if not callable(diamonds_4cs_rmse):
        fails('diamonds_4cs_rmse should be a function', mode)
    elif diamonds_4cs_rmse(np.zeros(len(some_arbitrary_weights))) != np.sqrt(np.mean(diamonds_4cs.column('price')**2)):
        fails('diamonds_4cs_rmse doesn\'t seem to be computing RMSE correctly.', mode)
    else:
        ok(mode)
    
def check13(best_weights_4cs, diamonds_4cs, diamonds_4cs_rmse, mode=CHECK):
    if not is_np_array(best_weights_4cs):
        fails('Your answer should be an array.', mode)
    elif len(best_weights_4cs) != diamonds_4cs.num_columns:
        fails('Your array does not have the correct number of elements.', mode)
    elif diamonds_4cs_rmse(best_weights_4cs) > diamonds_4cs_rmse(best_weights_4cs + 10):
        fails('The weights you found are not the best possible weights according to your diamonds_4cs_rmse function. Double check how you are minimizing.', mode)
    else:
        ok(mode)

        
