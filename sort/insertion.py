"""
Insertion sort
"""

import time
from range import *


ARRAY_SIZE: int = 10


def sort(array: list[int]) -> list[int]:

    for index_of_last_sorted_value in range(1, len(array)):
        index_of_current_value: int = index_of_last_sorted_value

        while array[index_of_current_value] < array[index_of_current_value - 1]:
            if index_of_current_value == 0:
                break

            current_value: int = array[index_of_current_value]
            array.pop(index_of_current_value)
            index_of_current_value -= 1
            array.insert(index_of_current_value, current_value)

    return array


array: list[int] = generate_array_of_number(ARRAY_SIZE)
print(f"Initial array : {array}")
start_time: float = time.time()
sorted_array: list[int] = sort(array)
stop_time: float = time.time()
print(f"Sorted array : {sorted_array}")
print(f"Spent {stop_time - start_time}s to sort array of {ARRAY_SIZE} values by insertion.")
