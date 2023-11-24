def sort(array: list[int]) -> list[int]:
    """Sorts the given array using insertion sort."""

    for i in range(1, len(array)):
        key: int = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array
