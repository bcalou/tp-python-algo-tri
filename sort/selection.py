def sort(array: list[int]) -> list[int]:
    """
    Sorts an array in ascending order using the selection sort algorithm.

    :param array: A list of integers to be sorted.
    :return: The sorted list.
    """
    for i in range(len(array)):
        min_index: int = i
        # Loop to find the index of the smallest element in the unsorted part of the array
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted part
        array[i], array[min_index] = array[min_index], array[i]
    return array
