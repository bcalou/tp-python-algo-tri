"""
Fusion sort
"""


def is_even(number: int) -> bool:
    return number % 2 == 0


def split_array_in_two(array: [int]) -> ([int], [int]):
    """Splits the given array into two arrays :
    if the array size is even the two parts will be the same size.
    if the array size is odd the second part will have one number more than the
    first one."""
    split_value = len(array) // 2
    return array[:split_value], array[split_value:]


def merge(first_array: list[int], second_array: list[int]) -> [int]:
    """Compare the first element of each sorted arrays"""
    sorted_array: [int] = []
    # Copy of the second array to be modified when the second array is iterated
    temporary_array: [int] = second_array[:]

    # for first_array_element in first_array:
    #     for second_array_element in second_array:
    #         if second_array_element < first_array_element:
    #             # If the element is smaller, it has to be placed in first and
    #             # removed from its original array
    #             sorted_array.append(second_array_element)
    #             temporary_array.remove(second_array_element)
    #
    #     sorted_array.append(first_array_element)
    #     # Erase second array with updated values
    #     second_array = temporary_array[:]

    i = j = k = 0
    while i < len(first_array) and j < len(second_array):
        if first_array[i] <= second_array[j]:
            sorted_array.append(first_array[i])
            i += 1
        else:
            sorted_array.append(second_array[j])
            j += 1
        k += 1

    while i < len(first_array):
        sorted_array.append(first_array[i])
        i += 1
        k += 1

    while j < len(second_array):
        sorted_array.append(second_array[j])
        j += 1
        k += 1

    # if len(first_array) > 0:
    #     # Append the remaining items of the second array at the end of the
    #     # array
    #     sorted_array += first_array
    #
    # if len(second_array) > 0:
    #     # Append the remaining items of the second array at the end of the
    #     # array
    #     sorted_array += second_array

    return sorted_array


def merge(first_array: list[int], second_array: list[int]) -> [int]:
    """Merge two sorted arrays in one sorted array"""

    # Init an array of the size of the two given arrays
    merged_array: list[int] = [0] * (len(first_array) + len(second_array))

    first_array_position = second_array_position = merged_array_position = 0

    # Compare each array values from left to right and put the smallest value
    # in the merged array first
    while first_array_position < len(
            first_array) and second_array_position < len(second_array):
        if (first_array[first_array_position] <=
                second_array[second_array_position]):
            merged_array[merged_array_position] = first_array[
                first_array_position]
            first_array_position += 1
        else:
            merged_array[merged_array_position] = second_array[
                second_array_position]
            second_array_position += 1
        merged_array_position += 1

    # if there is bigger elements remaining in each array, append it at the end
    # of the merged array
    while first_array_position < len(first_array):
        merged_array[merged_array_position] = first_array[first_array_position]
        first_array_position += 1
        merged_array_position += 1

    while second_array_position < len(second_array):
        merged_array[merged_array_position] = second_array[
            second_array_position]
        second_array_position += 1
        merged_array_position += 1

    return merged_array


def sort(array: list[int]) -> list[int]:
    # If the array contains one item, it is already sorted
    if len(array) > 1:
        # Split the array in two parts
        splitted_array: ([int], [int]) = split_array_in_two(array)
        # Merge both parts after sorting them
        array = merge(sort(splitted_array[0]), sort(splitted_array[1]))

    return array
