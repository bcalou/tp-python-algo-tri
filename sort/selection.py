"""
Selection sort
"""

import time
import random


array_size: int = 10


def sort(array: list[int]) -> list[int]:
    current_index_to_sort: int = 0

    for current_value_to_sort in array:
        index_of_lowest_value: int = 0
        lowest_value: int = 100
        
        # Only checking values in left part of array that hasn't been sorted yet
        for index, value in enumerate(array[current_index_to_sort:]):

            if value < lowest_value:
                lowest_value = value
                index_of_lowest_value = index

        # Switching the value located in the current index of work with the
        # lowest one of the non-sorted part.
        # Adding current_index_to_sort because index_of_lowest_value is a
        # relative index in the non-sorted part of the array.
        array[current_index_to_sort], array[index_of_lowest_value + current_index_to_sort] = (
            array[index_of_lowest_value + current_index_to_sort], array[current_index_to_sort])

        current_index_to_sort += 1

    return array


def generate_array_of_number(array_size: int) -> list[int]:
    return [random.randint(0, 100) for i in range(array_size)]


array: list[int] = generate_array_of_number(array_size)
print(f"Initial array : {array}")
start_time: float = time.time()
sorted_array: list[int] = sort(array)
stop_time: float = time.time()
print(f"Sorted array : {sorted_array}")
print(f"Spent {stop_time - start_time}s to sort array of {array_size} values by selection.")
