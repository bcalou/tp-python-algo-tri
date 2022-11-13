"""
Number generator
"""
import random
import time

MIN_RANGE: int = 0
MAX_RANGE: int = 100
BASE_GEN_NUMBER = 1_000


def generate_array_of_number(array_size: int) -> list[int]:
    """Generate array of specified size with range between MIN_RANGE and MAX_RANGE"""
    start: float = time.time()
    result_array: list[int] = [array_size]
    for number in range(array_size):
        result_array.append(random.randint(MIN_RANGE, MAX_RANGE))
    end: float = time.time()
    # print("Temps écoulé :", end - start)
    return result_array


tab_list: list[list[int]] = [generate_array_of_number(BASE_GEN_NUMBER * 1),
                             generate_array_of_number(BASE_GEN_NUMBER * 2),
                             generate_array_of_number(BASE_GEN_NUMBER * 3),
                             generate_array_of_number(BASE_GEN_NUMBER * 4),
                             generate_array_of_number(BASE_GEN_NUMBER * 5),
                             generate_array_of_number(BASE_GEN_NUMBER * 6),
                             generate_array_of_number(BASE_GEN_NUMBER * 7),
                             generate_array_of_number(BASE_GEN_NUMBER * 8),
                             generate_array_of_number(BASE_GEN_NUMBER * 9),
                             generate_array_of_number(BASE_GEN_NUMBER * 10)]
