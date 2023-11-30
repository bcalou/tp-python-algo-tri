import random


def generate_array_of_number(array_size: int) -> list[int]:
    """Return an array of numbers between 0 and 100 of the given size"""

    return [random.randint(0, 100) for i in range(array_size)]
