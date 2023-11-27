def sort(array: list[int]) -> list[int]:
    """Merge Sort Part 1:
    Continuously (recursively) split the given array in two,
    the result is merged and returned"""
    length = len(array)

    if length <= 1:
        return array

    # Split the array in two and sort each
    middle = length // 2
    left = sort(array[:middle])
    right = sort(array[middle:])

    # Merge the two sorted halves
    return merge(left, right)


def merge(left, right):
    """Merge Sort Part 2:
    Sort and merge two given halveds of an array"""
    merged_list = []
    left_i = 0
    right_i = 0

    # Merge the two lists while there are elements in both
    while left_i < len(left) and right_i < len(right):
        if left[left_i] < right[right_i]:
        # Place left element first as it's less than right element
            merged_list.append(left[left_i])
            left_i += 1
        else:
        # Place right element first as it's less than left element
            merged_list.append(right[right_i])
            right_i += 1

    # Takes the remaining elements in the slice 
    # and appends them to the end of merged_list (they're already sorted)
    merged_list.extend(left[left_i:])
    merged_list.extend(right[right_i:])

    return merged_list
