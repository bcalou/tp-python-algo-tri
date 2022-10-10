"""
Selection sort
"""


def sort(array: list[int]) -> list[int]:
    """Sort the list with a selection algorithm"""
    for reference_index, reference_number in enumerate(array):
        # Our reference number
        smallest_number: [int, int] = [reference_index, reference_number]

        # Compare the reference with every other number in the list after the
        # reference
        for compared_number_index, j in enumerate(array[reference_index + 1:]):
            if j < smallest_number[1]:
                smallest_number = [compared_number_index + reference_index + 1,
                                   j]

        # Exchange the smallest number found with the reference number in the
        # list
        array[reference_index] = smallest_number[1]
        array[smallest_number[0]] = reference_number

    return array
