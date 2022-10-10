"""
Selection sort
"""
import time


def sort(array: list[int]) -> list[int]:
    """Does a sort by selection"""
    start: float = time.time()
    # Go through each element of list
    array_length: int = len(array)
    for current_index, element in enumerate(array):
        min_element_index = current_index
        # For each posterior element of the list, we try to find if the element is inferior.
        # We must pass by a secondary sublist index,
        # to have an index based on the list and not the sublist
        for sublist_index in range(current_index + 1, array_length):
            if array[min_element_index] > array[sublist_index]:
                min_element_index = sublist_index
        # After finding the min, we exchange it with our current position
        array[current_index], array[min_element_index] = array[min_element_index], element
    end: float = time.time()
    print("Temps écoulé :", end - start)
    return array
