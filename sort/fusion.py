"""
Fusion sort
"""


def sort(array: list[int]) -> list[int]:
    if len(array) > 1:

        mid = len(array) // 2
        L = array[:mid]
        R = array[mid:]

        # Sorting the two halves
        sort(L)
        sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

        return array

    return array

