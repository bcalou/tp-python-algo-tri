"""
Number generator
"""
import random
import time

from sort.insertion import sort as insertion_sort
from sort.selection import sort as selection_sort
from sort.recursion import get_factorial
from sort.fusion import sort as fusion_sort


def generate_array_of_number(array_size: int) -> list[int]:
    return [random.randint(0, 100) for i in range(array_size)]


def get_10_random_arrays(start_size: int, step: int) -> list[list[int]]:
    """Returns 10 list of random int"""
    test_list: list[list[int]] = []

    for i in range(10):
        test_list.append(generate_array_of_number(start_size))
        start_size += step

    return test_list


# Generate 10 arrays of random ints with a size of 1000, 2000, 3000, ...
random_number_list = get_10_random_arrays(1000, 1000)

# For each array, we store the number of element in it for the key and the
# value is the time to perform the sort
execution_times: dict[int, float] = {}

for i in range(len(random_number_list)):
    start: float = time.time()

    # sorted_array: list[int] = selection_sort(random_number_list[i])
    # sorted_array: list[int] = insertion_sort(random_number_list[i])
    sorted_array: list[int] = fusion_sort(random_number_list[i])
    # random_number_list[i].sort()

    end: float = time.time()
    print(random_number_list[i])
    execution_times[i] = (end - start)

print(execution_times)
