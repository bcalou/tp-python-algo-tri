"""
Selection sort
"""

import time
from range import *


ARRAY_SIZE: int = 9000


def sort(array: list[int]) -> list[int]:

    for current_index_to_work_on in range(0, len(array) - 1):
        index_of_lowest_value: int = current_index_to_work_on

        # Only checking values in left part of array that hasn't been sorted yet
        for index in range(current_index_to_work_on, len(array)):

            if array[index] < array[index_of_lowest_value]:
                index_of_lowest_value = index

        # Switching the value located in the current index to work on with the
        # lowest one of the non-sorted part.
        array[current_index_to_work_on], array[index_of_lowest_value] = (
            array[index_of_lowest_value], array[current_index_to_work_on]
        )

    return array


array: list[int] = generate_array_of_number(ARRAY_SIZE)
print(f"Initial array : {array}")
start_time: float = time.time()
sorted_array: list[int] = sort(array)
stop_time: float = time.time()
print(f"Sorted array : {sorted_array}")
print(f"Spent {stop_time - start_time}s to sort array of {ARRAY_SIZE} values by selection.")
