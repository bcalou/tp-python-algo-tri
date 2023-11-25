import sort.insertion as insertion
import time


def sort(array: list[int]) -> list[int]:
    '''
        Return the array by using fusion sort
    '''

    if len(array) <= 1:
        return array
    else:
        half = len(array) // 2
        return merge(sort(array[:half]), sort(array[half:]))


def merge(array: list[int], array2: list[int]) -> list[int]:
    '''
        Merge two arrays by sorting them
    '''

    sorted_array = []

    array_index = 0
    array2_index = 0

    while len(sorted_array) != len(array) + len(array2):

        # Avoid list out of range
        if array_index >= len(array):

            sorted_array.append(array2[array2_index])
            array2_index += 1

        elif array2_index >= len(array2):

            sorted_array.append(array[array_index])
            array_index += 1

        # or check wich value is the smallest

        elif array2[array2_index] < array[array_index]:

            sorted_array.append(array2[array2_index])
            array2_index += 1

        elif array[array_index] <= array2[array2_index]:

            sorted_array.append(array[array_index])
            array_index += 1

    return sorted_array
