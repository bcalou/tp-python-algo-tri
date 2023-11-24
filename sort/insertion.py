def sort(array: list[int]) -> list[int]:
    """
    Sort the given array in ascending order using the insertion sort algorithm.

    :param array: The array to be sorted.
    :return: The sorted array.
    """
    for i in range(1, len(array)):
        value_to_insert: int = array[i]
        j: int = i - 1
        while j >= 0 and value_to_insert < array[j]:
            j -= 1
        array.insert(j + 1, array.pop(i))
    return array
