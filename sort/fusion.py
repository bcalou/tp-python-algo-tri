def sort(array: list[int]) -> list[int]:
    """
    Sorts an array in ascending order using the merge sort algorithm.

    :param array: The array to be sorted.
    :return: The sorted array.
    """
    if len(array) <= 1:
        return array

    # Divide the array into two halves and sort each half.
    mid: int = len(array) // 2
    left: list[int] = sort(array[:mid])
    right: list[int] = sort(array[mid:])

    return merge(left, right)


def merge(left_array: list[int], right_array: list[int]) -> list[int]:
    """
    Merge two lists in a sorted order.

    :param left_array: The first list to be merged.
    :param right_array: The second list to be merged.
    :return: A new list that is a sorted merge of the two input lists.
    """
    result: list[int] = []
    left_index: int = 0
    right_index: int = 0

    while left_index < len(left_array) and right_index < len(right_array):
        # Append the smaller element between
        # left_array[left_index] and right_array[right_index] to the result
        if left_array[left_index] < right_array[right_index]:
            result.append(left_array[left_index])
            left_index += 1
        else:
            result.append(right_array[right_index])
            right_index += 1

    # Append any remaining elements in left and right to the result
    result.extend(left_array[left_index:])
    result.extend(right_array[right_index:])
    return result
