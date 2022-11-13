"""
Insertion sort
"""
import time


def sort(array: list[int]) -> list[int]:
    """Sort by insertion"""

    # For each index of the array
    for current_index in range(0, len(array)):
        element_to_sort = array[current_index]
        # For each element before the element, we compare it to insert it
        for sub_index in range(current_index - 1, -1, -1):
            # If the element is inferior to current sub index
            # and superior to the sub index before,
            # exception if it equals 0
            if element_to_sort < array[sub_index] and (sub_index == 0 or
                                                       element_to_sort >= array[sub_index - 1]):
                array.pop(current_index)
                array.insert(sub_index, element_to_sort)
                break
    return array
