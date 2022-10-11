"""
Insertion sort
"""


def sort(array: list[int]) -> list[int]:
    for reference_index in range(1, len(array)):
        # The number we are testing
        reference_value = array[reference_index]
        # The index of the number before the tested number
        previous_value_index = reference_index - 1

        while reference_value < array[previous_value_index] and \
                previous_value_index >= 0:
            # If the number we are testing is smaller than its previous number,
            # we put the previous value at the number position
            array[previous_value_index + 1] = array[previous_value_index]
            previous_value_index -= 1

        # Our reference number is now greater than the number at
        # previous_value_index, so we put it after
        array[previous_value_index + 1] = reference_value

    return array
