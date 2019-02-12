# Function that measures the performance of other functions

from time import time

"""
@timer_function
def my_fun():
  #...
"""

def timer_function(f):
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print ('Elapsed time:',(end-start))
        return result
    return wrapper