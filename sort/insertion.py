"""
Insertion sort
"""


def sort(array: list[int]) -> list[int]:
    """Sort an array using the insertion algorithm"""
    for current_cell in range(len(array)):
        # Pivot where the current cell will be reinserted
        pivot_cell: int = current_cell

        # Check smaller number in previous cells until fining bigger number
        for checked_cell in reversed(range(current_cell)):
            if array[checked_cell] < array[current_cell]:
                break
            pivot_cell = checked_cell

        # The reinsert if needed
        if pivot_cell != current_cell:
            array.insert(pivot_cell, array.pop(current_cell))

    return array
