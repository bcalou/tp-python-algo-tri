"""
Fusion sort
"""

from unittest import result
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

    if len(array) <= 1:
        return array

    '''Divide array by 2'''
    separation: int = len(array) // 2
    array1: list[int] = array[0:separation]
    array2: list[int] = array[separation:len(array)]

    return merge(sort(array1), sort(array2))


def merge(array1: list[int], array2: list[int]) -> list[int]:
    '''Sort one by one'''
    result_array: list[int] = []
    while array1 and array2:
        if array1[0] < array2[0]:
            result_array.append(array1.pop(0))
        else:
            result_array.append(array2.pop(0))

    result_array.extend(array1)
    result_array.extend(array2)

    return result_array


main()
