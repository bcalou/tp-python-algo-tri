import random


def generate_array_of_number(array_size: int) -> list[int]:
    """
    Generates an array of random numbers

    :param array_size:
    :return: array of random numbers
    """
    return [random.randint(0, 100) for i in range(array_size)]
