"""
Number generator
"""
import random

def generate_array_of_number(array_size: int) -> list[int]:
    return [random.randint(0, 100) for _ in range(array_size)]
