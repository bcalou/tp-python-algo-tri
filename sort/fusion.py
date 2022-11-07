"""
Fusion sort
"""


def is_even(number: int) -> bool:
    return number % 2 == 0


def split_array_in_two(array: [int]) -> ([int], [int]):
    """Splits the given array into two arrays :
    if the array size is even the two parts will be the same size.
    if the array size is odd the first part will have one number more than the
    second one."""
    first_array_length: int = len(array) // 2 if is_even(len(array)) else len(
        array) // 2 + 1
    second_array_start: int = len(array) - first_array_length if is_even(
        len(array)) else len(array) - first_array_length + 1

    return array[:first_array_length], array[second_array_start:]


def merge(first_array: list[int], second_array: list[int]) -> [int]:
    """Compare the first element of each sorted arrays"""
    sorted_array: [int] = []
    # Copy of the second array to be modified when the second array is iterated
    temporary_array: [int] = second_array[:]

    for first_array_element in first_array:
        for second_array_element in second_array:
            if second_array_element < first_array_element:
                # If the element is smaller, it has to be placed in first and
                # removed from its original array
                sorted_array.append(second_array_element)
                temporary_array.remove(second_array_element)

        sorted_array.append(first_array_element)
        # Erase second array with updated values
        second_array = temporary_array[:]

    if len(second_array) > 0:
        # Append the remaining items of the second array at the end of the
        # array
        sorted_array = sorted_array + second_array

    return sorted_array


def sort(array: list[int]) -> list[int]:
    if len(array) > 1:
        # if the array contains more than 1 items, split it and
        # merge it back, sorted
        arrays: ([int], [int]) = split_array_in_two(array)
        array = merge(sort(arrays[0]), sort(arrays[1]))

    # An array with 1 item is already sorted
    return array
