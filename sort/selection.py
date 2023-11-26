def sort(input_list: list[int]) -> list[int]:
    """
    Selection sort algorithm

    :param input_list: The list to be sorted.
    :return: The sorted list.
    """
    # Iterate over the entire list
    for current_index in range(len(input_list)):
        # Assume the current index is the index of the smallest element
        min_index = current_index

        # Iterate over the rest of the list
        for comparison_index in range(current_index + 1, len(input_list)):
            # If a smaller element is found, update min_index
            if input_list[min_index] > input_list[comparison_index]:
                min_index = comparison_index

        # Swap the current element with the smallest element found in
        # the unsorted part of the list
        input_list[current_index], input_list[min_index] = input_list[
            min_index], input_list[current_index]

    # Return the sorted list
    return input_list
