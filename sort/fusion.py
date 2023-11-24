def merge(array_A: list[int], array_B: list[int]) -> list[int]:
    """sort and merge two given array"""

    merged_array: list[int] = []

    while len(array_A) != 0 or len(array_B) != 0:

        if len(array_A) == 0:
            merged_array.extend(array_B)
            break

        if len(array_B) == 0:
            merged_array.extend(array_A)
            break

        if array_A[0] < array_B[0]:
            merged_array.append(array_A[0])
            array_A.pop(0)
        else:
            merged_array.append(array_B[0])
            array_B.pop(0)

    return merged_array


def sort(array: list[int]) -> list[int]:
    """split the array until every element is separated"""

    if len(array) > 1:
        array = merge(sort(array[:len(array)//2]),
                      sort(array[len(array)//2:]))

    return array
