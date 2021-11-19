import random


def generate_random_list(length: int) -> list[int]:
    """ Generates and returns a list of random numbers and prints the process duration in seconds """
    array = [random.randint(0, 100) for i in range(length)]
    return array
