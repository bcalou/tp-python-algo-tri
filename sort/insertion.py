def sort(array: list[int]) -> list[int]:
    """Sort the array with insertion sort"""
    # For each item of the input array
    # (skip the first, which is the sorted part of the array at the start)
    for pivot_index in range(1, len(array)):

        # Go through the sorted part of the array in reverse (descending order)
        for sorted_index in reversed(range(pivot_index)):

            # When we find a value that is smaller than the one we're sorting,
            # we need to place the value we're sorting after it
            if array[sorted_index] < array[pivot_index]:

                # Move the value to its correct position and stop the for loop
                move(array, pivot_index, sorted_index + 1)
                break

        # If we tried every value of the sorted part and found none smaller
        # than the one we're sorting, if means that the value we're sorting
        # is the smallest so far. Place it at the start.
        else:
            move(array, pivot_index, 0)

    return array


def move(array: list, from_index: int, to_index: int) -> None:
    """Change the position of an element inside an array"""
    array.insert(to_index, array.pop(from_index))
