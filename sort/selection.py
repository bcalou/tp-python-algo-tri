def sort(array: list[int]) -> list[int]:
    """Sort the array with selection sort"""
    # For each item of the input array (skip the last, automatically sorted)
    for pivot_index in range(len(array) - 1):

        # For now, assume that the current element is the smallest
        index_of_smallest = pivot_index

        # For each element between the current element and the end of the array
        # (= the unsorted part of the array)
        for unsorted_index in range(pivot_index + 1, len(array)):

            # If the element is smaller than the smallest so far,
            # it becomes the new smallest
            if array[unsorted_index] < array[index_of_smallest]:
                index_of_smallest = unsorted_index

        # Exchange the position of the current element and the smallest element
        # found in the rest of the array, if necessary
        if pivot_index != index_of_smallest:
            array[pivot_index], array[index_of_smallest] =\
                array[index_of_smallest], array[pivot_index]

    return array
