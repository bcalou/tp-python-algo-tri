"""
Selection sort
"""


def sort(array: list[int]) -> list[int]:
    """Sort the list with a selection algorithm"""
    for reference_index, reference_number in enumerate(array):
        # Our reference number is the smallest at the beginning
        smallest_number: [int, int] = [reference_index, reference_number]

        # Comparing the reference with every other number in the list after the
        # reference
        for j in range(reference_index, len(array)):
            if array[j] < smallest_number[1]:
                smallest_number = [j, array[j]]

        # Exchange the smallest number found with the reference number in the
        # list
        array[reference_index], array[smallest_number[0]] = (smallest_number[1],
                                                             reference_number)

    return array
