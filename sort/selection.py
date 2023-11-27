def sort(array: list[int]) -> list[int]:
    """Selection Sort:
    Continuously explore a given list, compare adjacent elements and swaps them 
    if they are in the wrong order
    """

    # Determine the length of the array
    length = len(array)

    # Do length-1 turns through the array (breaks if finished = False)
    for turn in range(length - 1):
        # Flag to check if any swap has been made in this turn
        # (=> Iteration with no swap means that every element has been checked
        # and thus the array has every number in order)
        swap = False

        # Traverse the array from 0 to length-turn-1
        for i in range(length - turn - 1):
            i1 = i
            i2 = i + 1
            # Compare the current element with the next one
            if array[i1] > array[i2]:
                # Swap them if the current element is greater than the next one
                array[i1], array[i2] = array[i2], array[i1]
                # A swap was made
                swap = True

        # If no swaps were made, the array is sorted
        if not swap:
            break

    return array
