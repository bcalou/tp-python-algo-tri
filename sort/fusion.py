"""
Fusion sort
"""
import time


def sort(array: list[int]) -> list[int]:
    """Does a sort by fusion"""
    start: float = time.time()
    result_array: list[int] = sub_sort(array)
    end: float = time.time()
    print("Temps écoulé :", end - start)
    return result_array


def sub_sort(array: list[int]) -> list[int]:
    """Sub sort function to isolate the timer"""
    array_length: int = len(array)
    if array_length <= 1:
        return array
    return merge(sub_sort(array[:len(array) // 2]), sub_sort(array[len(array) // 2:]))


def merge(array_1: list[int], array_2: list[int]) -> list[int]:
    index_array_1: int = 0
    index_array_2: int = 0
    result_list: list[int] = []
    # we go through all the object of the list one by one
    while index_array_1 < len(array_1) and index_array_2 < len(array_2):
        if array_1[index_array_1] < array_2[index_array_2]:
            result_list.append(array_1[index_array_1])
            index_array_1 += 1
        else:
            result_list.append(array_2[index_array_2])
            index_array_2 += 1
    # After getting all data from a list, we concatenate the list rest
    if index_array_1 >= len(array_1):
        result_list += array_2[index_array_2:]
    elif index_array_2 >= len(array_2):
        result_list += array_1[index_array_1:]
    return result_list
