def merge(array_A: list[int], array_B: list[int]) -> list[int]:
    """sort and merge two given array"""

    merged_array: list[int] = []

    if len(array_A) == 0:
        return array_B

    if len(array_B) == 0:
        return array_A

    array_of_min: list[int] = array_A

    if array_A[0] > array_B[0]:
        array_of_min = array_B

    merged_array.append(array_of_min[0])
    if len(array_of_min) > 1:
        for value in (merge(array_of_min[1 : len(array_of_min)], 
                            array_A if array_of_min == array_B else array_B)):
            merged_array.append(value)

    return merged_array


def sort(array: list[int]) -> list[int]:
    """split the array until every element is separated"""

    if len(array) > 1:
        array = merge(sort(array[0 : len(array)//2]),
                      sort(array[len(array)//2 : len(array)]))

    return array
