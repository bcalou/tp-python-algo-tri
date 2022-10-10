"""
Number generator
"""
import random
import time


def generate_array_of_number(array_size: int) -> list[int]:
    return [random.randint(0, 100) for i in range(array_size)]


list_size: int = 1000000
execution_times: dict[int, float] = {}
for i in range(10):
    start: float = time.time()

    array: list[int] = generate_array_of_number(list_size)

    end: float = time.time()
    execution_times[list_size] = (end - start)
    list_size += 1000000

# {Number of element in the list: Time to do the task in seconds}
print(execution_times)
