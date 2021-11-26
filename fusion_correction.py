import time
import random

def sort(array: list[int]) -> list[int]:
    if len(array) <= 1:
        return array
    middle_index: int = len(array) // 2
    right_array = sort(array[middle_index:])
    left_array = sort(array[:middle_index])
    return merge(right_array, left_array)


def merge(left_array: list[int], right_array: list[int]) -> list[int]:
    index_left: int = 0
    index_right: int = 0

    sorted_array: list[int] = [] 

    while index_left < len(left_array) and index_right < len(right_array):
        if left_array[index_left] < right_array[index_right]:
            sorted_array.append(left_array[index_left])
            index_left += 1
        else:
            sorted_array.append(right_array[index_right])
            index_right += 1
    if index_left == len(left_array):
        sorted_array += right_array[index_right:]
    else:
        sorted_array += left_array[index_left:]

    # sorted_array += (right_array[index_right:] if index_left == len(left_array) else left_array[index_left:])

    return sorted_array

print(sort([2, 11, 5, 3, 6, 4, 10, 9]))    