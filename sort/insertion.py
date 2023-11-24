def sort(array: list[int]) -> list[int]:
    """Sorts the given array using insertion sort."""

    for index in range(1, len(array)):
        key: int = array[index]
        index_2 = index - 1
        while index_2 >= 0 and key < array[index_2]:
            array[index_2 + 1] = array[index_2]
            index_2 -= 1
        array[index_2 + 1] = key
    return array
