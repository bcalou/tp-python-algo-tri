"""
Fusion sort
"""


import time
from range import *


ARRAY_SIZE: int = 8000


def sort(array: list[int]) -> list[int]:
    if len(array) == 1:
        return array
    else:
        pivot: int = int(len(array) / 2)
        array1: list[int] = array[:pivot]
        array2: list[int] = array[pivot:]
        return merge(sort(array1), sort(array2))


def merge(array1: list[int], array2: list[int]) -> list[int]:
    result: list[int] = []

    while len(array1) > 0 and len(array2) > 0:
        if array1[0] < array2[0]:
            result.append(array1[0])
            array1.pop(0)
        else:
            result.append(array2[0])
            array2.pop(0)

    if len(array1) == 0:
        result.extend(array2)

    if len(array2) == 0:
        result.extend(array1)

    return result


array: list[int] = generate_array_of_number(ARRAY_SIZE)
print(f"Initial array : {array}")
start_time: float = time.time()
sorted_array: list[int] = sort(array)
stop_time: float = time.time()
print(f"Sorted array : {sorted_array}")
print(f"Spent {stop_time - start_time}s to sort array of {ARRAY_SIZE} values by fusion.")
