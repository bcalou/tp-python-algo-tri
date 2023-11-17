def sort(array: list[int]) -> list[int]:
    """Sorts the array using the insertion sort method."""
    # Arrays of size 0/1 are already sorted.
    if len(array) < 2:
        return array

    array_length: int = len(array)

    for i in range(array_length):
        # Skip first
        if i == 0:
            continue

        # Main logic loop
        new_index = i
        while new_index > 0:
            if array[new_index - 1] < array[i]:
                break

            new_index -= 1

        # Insert value right after the first number less than it
        value_to_insert = array.pop(i)
        array.insert(new_index, value_to_insert)

    return array
