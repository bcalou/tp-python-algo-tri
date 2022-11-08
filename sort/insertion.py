"""
Insertion sort
"""


import time
import random


array_size: int = 10


def sort(array: list[int]) -> list[int]:

    # print(len(array))

    for index_of_last_sorted_value in range(1, len(array)):
        index_of_current_value: int = index_of_last_sorted_value
        # print(f"Working on value {array[index_of_current_value]} at index {index_of_current_value}")

        while array[index_of_current_value] < array[index_of_current_value - 1]:
            if index_of_current_value == 0:
                break
            
            # print(f"Moving value {array[index_of_current_value]} from index {index_of_current_value} to index {index_of_current_value - 1}")
            current_value: int = array[index_of_current_value]
            array.pop(index_of_current_value)
            index_of_current_value -= 1
            array.insert(index_of_current_value, current_value)
            # print(array)
        
    return array


def generate_array_of_number(array_size: int) -> list[int]:
    return [random.randint(0, 100) for i in range(array_size)]


array: list[int] = generate_array_of_number(array_size)
print(f"Initial array : {array}")
start_time: float = time.time()
sorted_array: list[int] = sort(array)
stop_time: float = time.time()
print(f"Sorted array : {sorted_array}")
print(f"Spent {stop_time - start_time}s to sort array of {array_size} values by insertion.")