def sort(array: list[int]) -> list[int]:
    """sort using fusion:
    split the given list until every element is separated,
    then compare them to merge them into a sorted list"""

    if len(array) > 1:
        array = merge(sort(array[:len(array)//2]),
                      sort(array[len(array)//2:]))

    return array


def merge(array_a: list[int], array_b: list[int]) -> list[int]:
    """sort and merge two ordered given lists"""

    merged_array: list[int] = []

    while len(array_a) != 0 or len(array_b) != 0:

        if len(array_a) == 0:
            merged_array.extend(array_b)
            break

        if len(array_b) == 0:
            merged_array.extend(array_a)
            break

        if array_a[0] < array_b[0]:
            merged_array.append(array_a.pop(0))
        else:
            merged_array.append(array_b.pop(0))

    return merged_array
