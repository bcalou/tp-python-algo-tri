"""
Fusion sort
"""


def sort(array: list[int]) -> list[int]:
    if len(array) <= 1:
        return array

    # Split the array recusively
    array1: list[int] = sort(array[:int(len(array)/2)])
    array2: list[int] = sort(array[int(len(array)/2):])
    return merge(array1, array2)


def merge(array1: list[int], array2: list[int]):
    merged_array: list[int] = []
    # Merge the two presorted array step by step until one of the arrays is empty
    while len(array1) > 0 and len(array2) > 0:
        if array1[0] < array2[0]:
            merge_and_pop(merged_array, array1)
        else:
            merge_and_pop(merged_array, array2)

    # Add the rest from the non empty array
    if len(array1) == 0:
        merged_array += array2
    else:
        merged_array += array1

    return merged_array


def merge_and_pop(merged_array: list[int], array_from: list[int]):
    """Merge the first element of an array to merged array then delete this element from the original array"""
    merged_array.append(array_from[0])
    array_from.pop(0)
