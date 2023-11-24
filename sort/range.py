import time
import random


def generate_array_of_number(array_size: int) -> list[int]:
    """Returns an array of the given size with random
    numbers between 0 and 100."""

    array: list[int] = []
    for i in range(array_size):
        array.append(random.randint(0, 100))
    return array


def execution_time_for_array_of_numbers():
    """Prints the execution time for generating
    an array of numbers."""

    for i in range(1, 11):
        start: float = time.time()
        generate_array_of_number(1000000*i)
        end: float = time.time()
        print(f"Time to generate array of {1000000*i} numbers: {end - start}")
