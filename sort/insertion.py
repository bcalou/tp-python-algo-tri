def sort(array: list[int]) -> list[int]:
    """
    Sort the given array in ascending order using the insertion sort algorithm.

    :param array: The array to be sorted.
    :return: The sorted array.
    """
    for i in range(1, len(array)):
        key: int = array[i]
        j: int = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array
