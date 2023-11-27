def sort(array: list[int]) -> list[int]:
    """
    Insertion Sort: 
    Sort an array one element at a time by iteratively shift elements to their correct positions 
    in the array
    """

    # Determine the length of the array
    length = len(array)

    # The loop is starting from the second element, index 1
    for i in range(1, length):
        # The current element we're comparing against the last sorted element
        current_element = array[i]

        # Last sorted item idx needed to find the position where we need to put current element
        last_sorted_index = i-1

        # Shift elements of the sorted portion to the right if they are larger than current element
        while last_sorted_index >= 0 and array[last_sorted_index] > current_element:
            array[last_sorted_index+1] = array[last_sorted_index]
            last_sorted_index -= 1

        # Place current element into its correct position
        array[last_sorted_index + 1] = current_element

    return array
