def merge(left: list[int], right: list[int]) -> list[int]:
    """
    Merge two lists in a sorted order.

    :param left: The first list to be merged.
    :param right: The second list to be merged.
    :return: A new list that is a sorted merge of the two input lists.
    """
    result: list[int] = []
    i: int = 0
    j: int = 0

    while i < len(left) and j < len(right):
        # Append the smaller element between left[i] and right[j] to the result
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements in left and right to the result
    result.extend(left[i:])
    result.extend(right[j:])
    return result


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
