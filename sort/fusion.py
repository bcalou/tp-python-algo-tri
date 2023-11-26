def sort(input_list: list[int]) -> list[int]:
    """
    Merge sort algorithm

    :param input_list: The list to be sorted.
    :return: The sorted list.
    """
    if len(input_list) <= 1:
        return input_list

    # Split input_list in half
    middle = len(input_list) // 2
    left = sort(input_list[:middle])
    right = sort(input_list[middle:])

    return merge(left, right)


def merge(left_list: list[int], right_list: list[int]) -> list[int]:
    """Merge two sorted lists into one sorted list"""
    merged_result = []
    left_index = right_index = 0

    # Compare elements from left and right lists and add the smallest
    # one to the result
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] < right_list[right_index]:
            merged_result.append(left_list[left_index])
            left_index += 1
        else:
            merged_result.append(right_list[right_index])
            right_index += 1

    # Append the remaining elements from left and right lists
    merged_result.extend(left_list[left_index:])
    merged_result.extend(right_list[right_index:])

    return merged_result
