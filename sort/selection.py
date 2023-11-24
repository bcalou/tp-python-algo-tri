def sort(array: list[int]) -> list[int]:
    """
    selection sort algorithm

    :param array:
    :return: sorted array
    """
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]
    return array
