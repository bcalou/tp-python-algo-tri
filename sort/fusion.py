def sort(array: list[int]) -> list[int]:
    """
    Fusion sort algorithm

    :param array:
    :return: sorted array
    """
    if len(array) <= 1:
        return array

    # Split array in half
    middle = len(array) // 2
    left = sort(array[:middle])
    right = sort(array[middle:])

    return merge(left, right)


def merge(left: list[int], right: list[int]) -> list[int]:
    """Merge two sorted lists into one sorted list"""
    result = []
    i = j = 0

    # Compare elements from left and right lists and add the smallest
    # one to the result
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
