import random

def generate_array_of_number(array_size: int) -> list[int]:
    """Generate a random list of numbers
    """
    array = [random.randint(0, 100) for i in range(array_size)]
    return array
