"""
Selection sort
"""

import time
import random


array_size: int = 10


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
            array[index_of_lowest_value], array[current_index_to_work_on])

    return array


def generate_array_of_number(array_size: int) -> list[int]:
    return [random.randint(0, 100) for i in range(array_size)]


array: list[int] = generate_array_of_number(array_size)
# print(f"Initial array : {array}")
start_time: float = time.time()
sorted_array: list[int] = sort(array)
stop_time: float = time.time()
# print(f"Sorted array : {sorted_array}")
print(f"Spent {stop_time - start_time}s to sort array of {array_size} values by selection.")
