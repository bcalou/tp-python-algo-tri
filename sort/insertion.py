"""
Insertion sort
"""


def sort(array: list[int]) -> list[int]:
    """Sort an array using the insertion algorithm"""

    for current_case in range(len(array)):
        # Pivot where the current case will be reinserted
        pivot_case: int = current_case

        # Check smaller number in previous cases until fining bigger number
        for checked_case in reversed(range(current_case)):
            if array[checked_case] < array[current_case]:
                break
            pivot_case = checked_case

        # The reinsert if needed
        if pivot_case != current_case:
            array.insert(pivot_case, array.pop(current_case))

    return array
