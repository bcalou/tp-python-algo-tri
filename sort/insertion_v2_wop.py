"""
Insertion sort
"""


import time
from range import *


ARRAY_SIZE: int = 10


def sort(array: list[int]) -> list[int]:
    for index_of_current_value in range(1, len(array)):
        index_of_value_to_compare: int = index_of_current_value - 1
        print(f"Working on value {array[index_of_current_value]} at index {index_of_current_value}")

        while True:
            if index_of_value_to_compare < -1:
                break
            """elif index_of_value_to_compare == -1:
                array = move_value(array, index_of_current_value, 0)"""

            if array[index_of_current_value] < array[index_of_value_to_compare]:
                print(f"Value {array[index_of_current_value]} at index {index_of_current_value} is smaller than value {array[index_of_value_to_compare]} at index {index_of_value_to_compare}, trying next one")
                index_of_value_to_compare -= 1
            else:
                print(f"Value {array[index_of_current_value]} at index {index_of_current_value} is greater than value {array[index_of_value_to_compare]} at index {index_of_value_to_compare}, switching")
                array = move_value(array, index_of_current_value, index_of_value_to_compare + 1)
                break

    return array


def move_value(array: list[int], origin_index: int, destination_index: int) -> list[int]:
    """if origin_index == destination_index:
        return array"""

    print(f"Moving value {array[origin_index]} from index {origin_index} to index {destination_index} just before {array[destination_index]}")
    value: int = array[origin_index]
    array.pop(origin_index)
    array.insert(destination_index, value)
    print(array)
    return array


array: list[int] = generate_array_of_number(ARRAY_SIZE)
print(f"Initial array : {array}")
start_time: float = time.time()
sorted_array: list[int] = sort(array)
stop_time: float = time.time()
print(f"Sorted array : {sorted_array}")
print(f"Spent {stop_time - start_time}s to sort array of {ARRAY_SIZE} values by insertion.")
