"""
Selection sort
"""


from xmlrpc.client import MAXINT


def sort(array: list[int]) -> list[int]:
    """Sort using the selection sorting algorithm"""

    array_size: int = len(array)

    # Move a pivot where the current minimum will be placed
    for pivot in range(0, array_size):
        # Index of the current number with the minimum value
        minimum_index: int = pivot
        # Check the list to find the current minimum
        for current_value in range(pivot, array_size):
            if array[current_value] < array[minimum_index]:
                minimum_index = current_value

        # Switch the places between the current minimum and the pivot
        array[pivot], array[minimum_index] = array[minimum_index], array[pivot]

    return array
