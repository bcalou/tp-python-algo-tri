"""
Insertion sort
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

    for old_index in range(1, len(array)):
        index_to_place: int = 0
        while array[old_index] > array[index_to_place]:
            index_to_place += 1

        array.insert(index_to_place, array.pop(old_index))

    return array


main()
