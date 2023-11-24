import random


def generate_array_of_number(n: int) -> list:
    """
    Generate a list of random integers.
    :param n: The number of elements to generate in the array.
    :return: A list of random integers with 'n' elements.
    """
    array: list[int] = [random.randint(0, 100) for _ in range(n)]
    return array
