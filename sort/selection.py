def sort(array: list[int]) -> list[int]:
    """sort a given list by searching the lowest value again and again"""

    current_index: int = 0
    lowest_value_index: int = 0

    while current_index < len(array):
        lowest_value_index = current_index

        for index, value in enumerate(array[current_index:]):
            if value < array[lowest_value_index]:
                lowest_value_index = index + current_index

        array[current_index], array[lowest_value_index] = \
            array[lowest_value_index], array[current_index]

        current_index += 1
        lowest_value_index = current_index

    return array
