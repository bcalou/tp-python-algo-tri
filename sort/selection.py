"""
Selection sort
"""


from xmlrpc.client import MAXINT


def sort(array: list[int]) -> list[int]:
    array_size: int = len(array)
    for i in range(0, array_size):
        current_minimum: int = MAXINT
        current_minimum_index: int = i
        for j in range(i, array_size):
            if array[j] < current_minimum:
                current_minimum = array[j]
                current_minimum_index = j
        array.insert(i, array.pop(current_minimum_index))

    return array
