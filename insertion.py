import time
import random

def insertion_sort(array: list[int]) -> list[int]:
    for index in range(1, len(array)):
        start_value: int = array[index]
        current_index: int = index - 1
        while current_index >= 0 and start_value < array[current_index] :
            array[current_index + 1] = array[current_index]
            current_index -= 1
        array[current_index + 1] = start_value
    print(array)
    return array


array = [6, 5, 3, 1, 8, 7, 2, 4]
insertion_sort(array)