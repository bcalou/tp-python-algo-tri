import random


def generate_array_of_number(array_size: int) -> list[int]:
    """Generate an array of random numbers between 0 and 100"""
    array = [random.randint(0, 100) for i in range(array_size)]

    return array
