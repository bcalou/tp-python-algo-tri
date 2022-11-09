"""
Python's sort()
"""


import time
from range import *


ARRAY_SIZE: int = 4000


array: list[int] = generate_array_of_number(ARRAY_SIZE)
print(f"Initial array : {array}")
start_time: float = time.time()
array.sort()
stop_time: float = time.time()
print(f"Sorted array : {array}")
print(f"Spent {stop_time - start_time}s to sort array of {ARRAY_SIZE} values by Python's sort() function.")
