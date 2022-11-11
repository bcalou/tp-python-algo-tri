"""
Selection sort
"""

import time
import range as range_array


def main():
    '''Function to evaluate the algorithm complexity'''
    for size in range(1, 11):
        array: list = range_array.generate_array_of_number(size * 1000)
        start: float = time.time()
        sort(array)
        end: float = time.time()
        print("Taille de tableau : ", size * 1000,
              " Temps écoulé :", end - start)


def sort(array: list[int]) -> list[int]:
    '''sort selection algorithm'''

    for iterator in range(len(array)):

        buffer_index: int = iterator

        for index in range(iterator, len(array)):
            if (array[index] < array[buffer_index]):
                buffer_index = index

        array[iterator], array[buffer_index] = \
            array[buffer_index], array[iterator]

    return array


main()
