import random
import time


def generate_array_of_number(n: int) -> list:
    """
    :param n: The number of elements to generate in the array.
    :return: A list of random integers with 'n' elements.
    """
    array: list[int] = [random.randint(0, 100) for _ in range(n)]
    return array


for i in range(10):
    start: float = time.time()
    generate_array_of_number(1_000_000 * (i + 1))
    end: float = time.time()
    print(f"Size: {1_000_000 * (i + 1)}, Time: {end - start} seconds")