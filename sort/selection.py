"""
Selection sort
"""


def sort(array: list[int]) -> list[int]:
    """Sort the list with a selection algorithm"""
    for reference_index, reference_number in enumerate(array):
        # Our reference number is the smallest at the beginning
        smallest_number_index: int = reference_index

        # Comparing the reference with every other number in the list after the
        # reference
        for tested_number_index in range(reference_index, len(array)):
            if array[tested_number_index] < array[smallest_number_index]:
                smallest_number_index = tested_number_index

        # Exchange the smallest number found with the reference number in the
        # list
        array[reference_index], array[smallest_number_index] = \
            array[smallest_number_index], reference_number

    return array
