"""
Insertion sort
"""


def sort(array: list[int]) -> list[int]:
    """Sort by insertion"""
    # position: int = 0
    print(array)
    for array_index in range(0, len(array)):
        element_to_sort = array[array_index]
        for subarray_index in range(array_index - 1, -1, -1):
            if element_to_sort < array[subarray_index] and (subarray_index == 0 or
                                                            element_to_sort >= array[subarray_index - 1]):
                array.pop(array_index)
                array.insert(subarray_index, element_to_sort)
                print(array)
                break
    return array
