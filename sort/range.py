"""
Number generator
"""

import random
import time


def main():
    '''Function to evaluate the algorithm complexity'''
    for size in range(1, 11):
        start: float = time.time()
        generate_array_of_number(size * 1_000_000)
        end: float = time.time()
        print("Taille de tableau : ", size * 1_000_000,
              " Temps écoulé :", end - start)


def generate_array_of_number(array_size: int) -> list[int]:
    return [random.randint(0, 100) for i in range(array_size)]


main()
