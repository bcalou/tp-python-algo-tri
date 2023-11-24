def merge(left: list[int], right: list[int]) -> list[int]:
    """Merges two sorted arrays into one sorted array."""

    result: list[int] = []
    left_index: int = 0
    right_index: int = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


def sort(array: list[int]) -> list[int]:
    """Sorts the given array using fusion sort."""

    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = sort(array[:mid])
    right_half = sort(array[mid:])

    return merge(left_half, right_half)
