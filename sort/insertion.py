def sort(input_list: list[int]) -> list[int]:
    """
    Insertion sort algorithm

    :param input_list: The list to be sorted.
    :return: The sorted list.
    """
    for current_index in range(1, len(input_list)):
        current_value = input_list[current_index]
        position = current_index

        # Find the right position for current_value
        while position > 0 and current_value < input_list[position - 1]:
            position -= 1

        # Once the right position is found, shift all elements between
        # position and current_index to the right by one.
        if position != current_index:
            for i in range(current_index, position, -1):
                input_list[i] = input_list[i - 1]

            # Place the current_value at its correct position
            input_list[position] = current_value

    return input_list
