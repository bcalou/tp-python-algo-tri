"""
Number generator
"""
import random


def generate_array_of_number(array_size: int) -> list[int]:
    array = [random.randint(0, 100) for i in range(array_size)]
    return array


def generate_array_of_number_time(array_size: int) -> list[int]:
    array = [random.randint(0, 100) for i in range(array_size)]
    return array
