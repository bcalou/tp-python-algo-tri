"""
Number generator
"""

import random
import time

array_size: int = 10_000_000


def generate_array_of_number(array_size: int) -> list[int]:
    return [random.randint(0, 100) for i in range(array_size)]


start_time: float = time.time()
array: list[int] = generate_array_of_number(array_size)
stop_time: float = time.time()
print(f"Spent {stop_time - start_time}s to generate array of {array_size} values.")
