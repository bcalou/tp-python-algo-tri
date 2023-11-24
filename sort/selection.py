def sort(array: list[int]) -> list[int]:
    """Sorts the given array using the selection sort method."""
    # Arrays of size 0/1 are already sorted.
    if len(array) < 2:
        return array

    array_length: int = len(array)

    for i in range(array_length - 1):
        # Sorting iteration loop
        min_index: int = i
        for j in range(i, array_length):
            min_index = j if array[j] < array[min_index] else min_index

        # If the current index is already sorted, do nothing.
        if min_index != i:
            # Swap the minimum and current numbers
            array[i], array[min_index] = array[min_index], array[i]

    return array
