"""
Number generator
"""
import random


def generate_array_of_number(array_size: int) -> list[int]:
    random_array: list[int] = []
    for i in range(array_size):
        random_array.append(random.randrange(0, 100))
    return random_array
