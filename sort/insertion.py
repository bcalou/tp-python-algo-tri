"""
Insertion sort
"""


def sort(array: list[int]) -> list[int]:

    # i and j are simply indices
    for i in range(1, len(array)):

        curr = array[i]
        j = i - 1
        while j >= 0 and curr < array[j]:
            array[j + 1] = array[j] # table shifting
            j -= 1

        array[j + 1] = curr

    return array
