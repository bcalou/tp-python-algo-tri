def sort_by_insertion(input_list: list[int]) -> list[int]:
    last_sorted_index = 0

    for last_sorted_index, current_value in enumerate(input_list):
        for compare_index in range(last_sorted_index - 1, -1, -1):
            compare_value = input_list[compare_index]
            if compare_value < current_value:
                break
            input_list[compare_index +
                       1], input_list[compare_index] = input_list[compare_index], input_list[compare_index + 1]

    return input_list
