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
        
###############################################################################################
    

def check1_1(b_pop, mode=CHECK):
    if not check_table_labels(b_pop, ('time', 'population_total'), mode):
        pass
    elif not np.array_equal(b_pop.sort("time").column("time"),np.arange(1970, 2015+1)):
        fails('Incorrect. Double check that you have the rows for the years 1970 though 2015.', mode)
    else:
        ok(mode)

def check1_2(b_five_growth, mode=CHECK):
    if not check_table_labels(b_five_growth, ('time', 'population_total', 'annual_growth'), mode):
        pass
    elif is_close(np.absolute(b_five_growth.column('annual_growth')).sum(), 0.0):
        fails('Incorrect. The growth rate should not be zero. You might be using the same values for initial and changed.', mode)
    elif is_close(round(b_five_growth.sort('time').column('annual_growth').item(0),4), .0962):
        fails('Incorrect. Make sure you are computing the *annual* growth rate (see the textbook).', mode)
    elif is_close(round(b_five_growth.sort('time').column('annual_growth').item(0),4), 1.8541):
        fails('Incorrect. You might be incorrectly multipliying by 100.', mode)
    else:
        ok(mode)

def check1_5(fertility_over_time, mode=CHECK):
    usa2010 = fertility_over_time('usa', 2010)
    if not check_table_labels(usa2010, ('Year', 'Children per woman'), mode):
        pass
    elif not np.array_equal(usa2010.sort('Year').column('Year'), np.arange(2010, 2015+1)):
        fails('Incorrect. Make sure to include the starting year.', mode)
    else:
        ok(mode)

def check1_7(fertility_and_child_mortality, mode=CHECK):
    if not check_table_labels(fertility_and_child_mortality, ('Children per woman', 'Child deaths per 1000 born'), mode):
        pass
    elif fertility_and_child_mortality.num_rows != 46:
        fail('Incorrect. Make sure the table contains data for each year from 1970 to 2015, inclusive.', mode)
    else:
        ok(mode)
        
def check1_9(fertility_statements, mode=CHECK):
    check_select_all_that_apply(fertility_statements, 6, mode)
    
def check1_11(stats_for_year, mode=CHECK):
    stats1990 = stats_for_year(1990)
    if not check_table_labels(stats1990, ('geo', 'population_total', 'children_per_woman_total_fertility', 'child_mortality_under_5_per_1000_born'), mode):
        pass
    elif stats1990.num_rows != 50:
        fails('Incorrect. There should be 50 rows.', mode)
    else:
        yem_stats = np.round(list(stats1990.where('geo', 'yem').to_array()[0])[1:4],1)
        if not is_close(yem_stats, [  1.20570390e+07,   8.70000000e+00,   1.24800000e+02]).all():
            fails('Incorrect. We spot checked Yemen in the year 1990, but the statistics look incorrect.', mode)
        else:
            ok(mode)

def check1_12(pop_by_decade, mode=CHECK):
    if not check_table_labels(pop_by_decade, ('decade', 'population'), mode):
        pass
    elif not np.array_equal(pop_by_decade.sort('decade').column('decade'), np.arange(1960, 2011, 10)):
        fails('Incorrect. It looks like you do not have the right years in the decades column.', mode)
    elif not (2e9 <= pop_by_decade.column('population').sum() <= 36e9):
        fails('Incorrect. The populations you computed seem to be way too small or way too big.', mode)
    else:
        ok(mode)    
    
def check1_13(region_counts, mode=CHECK):
    if not check_table_labels(region_counts, ('region', 'count'), mode):
        pass
    elif region_counts.column('count').sum() != 50:
        fails('Incorrect. The counts should sum to 50.', mode)
    else:
        ok(mode)

def check1_14(scatter_statements, mode=CHECK):
    check_select_all_that_apply(scatter_statements, 5, mode)
    
def check2_1(latest, mode=CHECK):
    if not check_table_labels(latest, ('geo', 'time', 'poverty_percent'), mode):
        pass
    elif latest.num_rows != 131:
        fails('Incorrect. The table should have one row per country.', mode)
    else:
        ok(mode)
        
def check2_2(recent, mode=CHECK):
    if not check_table_labels(recent, 
                             ('geo', 'poverty_percent', 'population_total', 'poverty_total'),
                             mode):
        pass
    elif recent.where('geo', 'ago').column('population_total').item(0) != 23369131:
        fails('Incorrect. The population of Angola should be 23,369,131.', mode)
    elif recent.where('geo', 'ago').column('poverty_total').item(0) != 7041119:
        fails('Incorrect. The number of people in extreme poverty in Angola should be 7,041,119. Did you round?', mode)
    else:
        ok(mode)
    
def check2_3(poverty_percent, mode=CHECK):
    if not (is_number(poverty_percent) and 0 <= poverty_percent <= 100):
        fails('Incorrect. Your answer should be a number between 0 and 100.', mode)
    else:
        ok(mode)
    
def check2_4(poverty_map, mode=CHECK):
    if not check_table_labels(poverty_map, 
                              ('name', 'region', 'latitude', 'longitude', 'poverty_total'), 
                              mode):
        pass
    elif poverty_map.num_rows != 130:
        fails('Incorrect. There should be 130 rows in the table.', mode)
    else:
        ok(mode)
        
def check2_5(largest, mode=CHECK):
    if not check_table_labels(largest, ('name', 'poverty_total'), mode):
        pass
    elif largest.num_rows != 10:
        fails('Incorrect. The table should have 10 rows.', mode)
    elif largest.sort('poverty_total', descending=True).column('name').item(0) != 'India':
        fails('Incorrect. The country with the largest number of people in extreme poverty is India.', mode)
    else:
        ok(mode)
    
def check2_6(country_poverty, mode=CHECK):
    if not check_fruitful_function(country_poverty, 'India', mode):
        pass
    else:
        india = country_poverty('India')
        if not check_table_labels(india, ('Year', 'Number in poverty'), mode):
            pass
        elif list(country_poverty('India').column('Year')) != [1983, 1987, 1993, 2004, 2009, 2011]:
            fails('Incorrect. The years in the table for India should be: 1983, 1987, 1993, 2004, 2009, 2011.', mode)
        elif not is_close(country_poverty('India').sort('Year').column('Number in poverty').item(0), 402306767):
            fails('Incorrect. The number of people in poverty in India in 1983 should be 402306767.', mode)
        else:
            ok(mode)
    
        