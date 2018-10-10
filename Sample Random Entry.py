import numpy as np

def index_check(index_j, array_test):
"""checks if entry in list/array exists"""
    try:
        array_test[index_j]
        status = True 
    except:
        status = False
        
    return status

def random_sample(long_array):
"""randomly samples single entry uniformly from a list/array while only storing one entry"""
    stored_value = long_array[0]
    count = 1
    
    while index_check(count, long_array):
        if np.random.uniform(0, 1, 1) < (1/(count + 1)):
            stored_value = long_array[count]
        count += 1
            
    return stored_value
