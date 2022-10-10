"""
Selection sort
"""


def sort(array: list[int]) -> list[int]:

    for i in range(len(array)):
        # We find the index of the min value of the array
        min = i
        for j in range(i + 1, len(array)):
            if array[min] > array[j]:
                min = j

        array[i], array[min] = array[min], array[i]

    return array
